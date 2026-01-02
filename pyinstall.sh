#!/bin/bash

# pyinstall: A utility to install Python packages and update requirements files.
#
# This script installs Python packages using pip and updates either
# 'requirements.txt' (for runtime dependencies) or 'dev-requirements.txt'
# (for development dependencies) with the installed package and its version.
#
# Usage:
#   ./pyinstall.sh [--dev] package1 [package2 ...]
#
# Examples:
#   ./pyinstall.sh requests
#   ./pyinstall.sh --dev pytest black
#
# Note: This script adds/updates top-level dependencies with their installed versions.
# It does not manage transitive dependencies or complex version conflicts.
# For more robust dependency management, consider tools like pip-tools.

pyinstall_function () {
  local dev_flag=0
  local packages=()
  local target_file="requirements.txt"
  local temp_file="${TMPDIR:-/tmp}/pyinstall_reqs_temp_$$" # Use TMPDIR for portability

  # Parse arguments: check for --dev flag and collect package names
  for arg in "$@"; do
    case "$arg" in
      --dev)
        dev_flag=1
        target_file="dev-requirements.txt"
        ;;
      *)
        packages+=("$arg")
        ;;
    esac
  done

  # Check if any package names were provided
  if [ ${#packages[@]} -eq 0 ]; then
    echo "Usage: pyinstall [--dev] package1 [package2 ...]"
    return 1
  fi

  # Install packages using pip
  echo "Installing packages: ${packages[@]}..."
  pip install "${packages[@]}"
  if [ $? -ne 0 ]; then
    echo "pip install failed for some packages. Please check the error messages above."
    return 1
  fi

  # Ensure the target requirements file exists
  touch "$target_file"

  echo "Updating $target_file with installed packages..."

  # Determine the installed version for each package
  local pkgs_to_add=()
  for pkg in "${packages[@]}"; do
    # Use 'pip show' to get the installed version; 'awk' to extract it
    local version=$(pip show "$pkg" 2>/dev/null | awk '/^Version:/ {print $2}')
    if [ -n "$version" ]; then
      pkgs_to_add+=("${pkg}==${version}")
    else
      echo "Warning: Could not find version for '$pkg'. This package will not be added to $target_file."
    fi
  done

  # If no packages had detectable versions, there's nothing to add to the file
  if [ ${#pkgs_to_add[@]} -eq 0 ]; then
    echo "No packages with detectable versions to add to $target_file."
    return 0
  fi

  # --- Update the requirements file ---
  # This process ensures existing entries for the packages are updated, and new ones are added.

  # 1. Construct a regex to filter out old lines for the packages being updated (case-insensitive)
  local filter_regex=""
  for pkg_name in "${packages[@]}"; do
    # Escape special regex characters in the package name
    local escaped_pkg_name=$(echo "$pkg_name" | sed 's/[][\/.^$*+?(){}|-]/\\&/g')
    filter_regex+="^${escaped_pkg_name}(==.*)?$|"
  done
  # Remove the trailing '|' from the regex
  filter_regex="${filter_regex%|}"

  # 2. Filter out existing lines from the target file and write to a temporary file
  #    Using 'grep -v -i -E' for case-insensitive exclusion with extended regex
  if [ -n "$filter_regex" ]; then
    grep -v -i -E "$filter_regex" "$target_file" > "$temp_file"
  else
    # If no packages were successfully processed, just copy the original content
    cp "$target_file" "$temp_file"
  fi

  # 3. Append the new/updated package lines (e.g., "package==version") to the temporary file
  for pkg_line in "${pkgs_to_add[@]}"; do
    echo "$pkg_line" >> "$temp_file"
  done

  # 4. Sort the temporary file contents alphabetically, remove duplicates, and write back to the target file
  sort -u "$temp_file" > "$target_file"
  rm "$temp_file" # Clean up the temporary file

  echo "Successfully updated $target_file."
  echo "Note: This script adds/updates top-level dependencies with their installed versions. It does not manage transitive dependencies or complex version conflicts. For more robust dependency management, consider tools like pip-tools."
}

# Call the function with all arguments passed to the script
pyinstall_function "$@"

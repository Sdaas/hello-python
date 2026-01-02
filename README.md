
# Context

This is a boilerplate repo for setting up python and jupyter notebook based projects.

# Table of Contents
<!-- 
Generating TOC from Markdown in Visual Studio Code requires the "Markdown TOC" extension from
Joffery Kern (https://marketplace.visualstudio.com/items?itemName=JoffreyKern.markdown-toc). There
are other extensions that do the same thing, but this is the one I found that works well.

Procedure for generating TOC in Visual Code
- Install the "Markdown TOC" extension from Joffery Kern
- Open this README.md file in Visual Studio Code
- Open the command palette (Cmd+Shift+P)
- Type "Generate"
- Choose "Generate TOC for markdown"

Note 
- The TOC is generated only for H2 and below. 
- Specifically, TOC is NOT generated for H1.
- The following section is auto-generated. dont muck with it
-->

<!-- vscode-markdown-toc -->
* [Jump Start for the Impatient](#JumpStartfortheImpatient)
* [Important Files and Folders](#ImportantFilesandFolders)
* [Developer Setup](#DeveloperSetup)
	* [Python Setup](#PythonSetup)
	* [Visual Code Setup](#VisualCodeSetup)
	* [Setup Pre-Commit Hook to Clear the output of Notebooks](#SetupPre-CommitHooktoCleartheoutputofNotebooks)
	* [Setup the Virtual Environment](#SetuptheVirtualEnvironment)
	* [Installing and managing dependencies](#Installingandmanagingdependencies)
	* [Useful Packages](#UsefulPackages)
		* [pytest](#pytest)
		* [python-dotenv](#python-dotenv)
	* [Testing](#Testing)
		* [Logging with Pytest](#LoggingwithPytest)
	* [Coverage Tests](#CoverageTests)
	* [Mutation Tests](#MutationTests)
	* [Jupyter Setup](#JupyterSetup)
		* [Using packages in editable mode](#Usingpackagesineditablemode)
		* [nbconvert](#nbconvert)
* [Other Developer Notes](#OtherDeveloperNotes)
	* [Configure the Git user for this repo](#ConfiguretheGituserforthisrepo)
	* [Setup SSH keys for Github](#SetupSSHkeysforGithub)
* [Resources](#Resources)
* [Scratchpad](#Scratchpad)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='JumpStartfortheImpatient'></a>Jump Start for the Impatient

- Add `FOO=bar` to the `.env` file
- Create a virtual environment - `virtualenv .venv`
- Activate it - `source .venv/bin/activate`
- Install dependencies - `pip install -r requirements.txt`
- Install developer dependencies - `pip install -r dev-requirements.txt`
- Command Line
    - Run all the tests - `pytest -v`
    - Run the app - `python app.py`
- Jupyter Notebooks
    - Register the virtual environment with Jupyter
    ```bash
    python -m ipykernel install --user --name=hello-python --display-name "Python (hello-python)"
    ```
    - Launch Jupyter notebook server - `jupyter notebook`
    - Make sure to use the correct kernel - "Python (hello-python)"
    - Run `notebooks/app.ipynb`


## <a name='ImportantFilesandFolders'></a>Important Files and Folders

- `app.py` - Main application file
- `calculator` - Sample package
- `setup.py` - Setup file for all the packages
- `requirements.txt` - all dependencies
- `dev-requirements.txt` - all developer dependencies including Jupyter
- `pyinstall.sh` - Script to install new packages and update requirements files
- `pre-commit` - Pre-commit hook to clear notebook outputs. Copy this to `.git/hooks/pre-commit` and make it executable
- `tests` - All unit tests are in this folder
- `notebooks` - Jupyter notebooks go here
- `.env` - Environment variables go here (don't check into git pls)

## <a name='DeveloperSetup'></a>Developer Setup
### <a name='PythonSetup'></a>Python Setup

We basically need to install `python` and `virtualenv`, and we will manage this using `pyenv`. 

- List all the versions of python 3.x `pyenv install --list | grep " 3\." `
- Install specific version of python. For example `pyenv install 3.10.6` 
- Use the `pyenv versions` command to list the locally installed version(s)
- Use `pyenv global 3.10.6` to use this version of Python Globally
- Install virtualenv `pip install virtualenv`

### <a name='VisualCodeSetup'></a>Visual Code Setup

Install the following Extensions

- Markdown TOC Extension from Joffery Kern (https://marketplace.visualstudio.com/items?itemName=JoffreyKern.markdown-toc)
- Python Extension for Visual Studio Code

### <a name='SetupPre-CommitHooktoCleartheoutputofNotebooks'></a>Setup Pre-Commit Hook to Clear the output of Notebooks

- `mkdir -p .git/hooks` 
-  `cp pre-commit .git/hooks/pre-commit` 
- Make it executable `chmod +x .git/hooks/pre-commit `
- Now, before every commit, any staged .ipynb files will have their output cleared automatically.

### <a name='SetuptheVirtualEnvironment'></a>Setup the Virtual Environment    

- See https://sourabhbajaj.com/mac-setup/Python/virtualenv.html 
- Install virtualenv - `pip install virtualenv `
- Go to the project root directory ...
- Create a virtual environment - `virtualenv .venv`. You can have any name for the virtual env but `.venv` is recognized automatically by many tools.
- Activate it - `source .venv/bin/activate` 
- At this point running `which pip` and `which python` will point to the specific versions that were used to setup the environment. Similarly running `pip list` will show only the packages installed in this virtual env.
- To exit the virtualenv, run `deactivate`


Note

- To Update the environment requirements - `pip freeze > requirements.txt` and check this into git
- Sometimes Jupyter notebook will not find a freshly installed packages. To fix this, just
`deactivate` and then reactivate the virtual environment.


### <a name='Installingandmanagingdependencies'></a>Installing and managing dependencies

All runtime dependencies should be listed in `requirements.txt` file. All developer dependencies (like Jupyter, pytest, etc) should be listed in `dev-requirements.txt` file.

- Make sure that the virtual environment is activated.
- Install all dependencies - `pip install -r requirements.txt`
- Install all the developer dependencies - `pip install -r dev-requirements.txt`
- All these dependencies will be installed in the virtual environment.

To install a new package, run `pip install xxx` and then append it to the correct requirements file.

Alternately, run the `./pyinstall.sh` script below to install packages and update the requirements file automatically.
```
./pyinstall.sh requests # Also updates requirements.txt
./pyinstall.sh --dev black flake8 # Also updates dev-requirements.txt
```

### <a name='UsefulPackages'></a>Useful Packages
This repo is already setup with some useful packages. Here are some of them

#### <a name='pytest'></a>pytest

Testing framework. See the section on [Testing](#Testing) for more details on how to use `pytest`.
Also see https://docs.pytest.org/en/7.4.x/

#### <a name='python-dotenv'></a>python-dotenv

`python-dotenv`  reads key-value pairs from a `.env` file and can set them as environment variables.
- Reads each key-value pair and add it to `os.environ`.
- Does NOT override an environment variable that is already set, unless called with `override=True`.
- See https://pypi.org/project/python-dotenv/ 
- Warning : Don't use dotenv - thats an older and incorrect package
- `pip install python-dotenv`or simply use `pyinstall python-dotenv` if you have added the snippet above

Sample code
```
from dotenv import load_dotenv
import os

# Load from .env file in the current directory
load_dotenv()
# Access the variable
foo = os.getenv("FOO")
```

### <a name='Testing'></a>Testing

All tests are in the `tests` directory. The tests are written using `pytest`.

There is also a `conftest.py` file in the `tests` directory which is used to configure the test environment. Its primary purpose here is to modify the Python system path (sys.path)
to ensure that modules in the parent directory (the project root) are
discoverable by tests located within this 'tests/' directory.

To run the tests, make sure that the virtual environment is activated, and then run the following command:


```bash
pytest -v # Runs all the test files in the tests directory
pytest tests/foo.py -v # Runs all the tests in tests/foo.py
pytest tests/foo.py::test_bar -v # Runs the test_bar function in tests/foo.py
pytest tests/foo.py -v -k "not bar" # Runs all tests in foo.py except those that have "bar" in their name
```

Note
- By default, pytest will discover all files that start with `test_` or end with `_test.py` in the `tests` directory.
- You can also run `pytest` without any arguments to run all tests in the `tests` directory.
- The `-v` flag is for verbose output, which prints the name of each test as it runs.
- By default, pytest suppresses output from passing tests. Use `-s` or `-v -s` flag to see print statements in the output
- Alternately, use `logging` as shown below

#### <a name='LoggingwithPytest'></a>Logging with Pytest

Use `logging` ...

```python
import logging
...
def test_logging():
    # Get and print the current working directory
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.error("this is an error")
```
By default, this will print only `ERROR` message to the console, and ONLY if the test fails.

To see all the log messages regardless of whether the test passes or fails, run

```bash
pytest -v --log-cli-level=INFO
```
### <a name='CoverageTests'></a>Coverage Tests

Test coverage is done via [coverage](https://coverage.readthedocs.io/en/latest/)
```bash
coverage run -m pytest # run the tests with coverage
coverage report -m  # generate a coverage report
coverage html  # generate an HTML report
```

### <a name='MutationTests'></a>Mutation Tests

Mutation testing is done via [mutmut](https://mutmut.readthedocs.io/en/latest/). 

- The `setup.cfg` file is already configured for mutmut
- First run coverage tests `coverage run -m pytest`. ( since `setup.cfg` says `use_coverage=True`)
- Run mutation tests `mutmut run`
- View the results `mutmut results`

This will generate a report like
```
app.x_get_foo_value__mutmut_7: survived
app.x_main__mutmut_1: no tests
calculator.x_factorial__mutmut_6: survived
```
- Run `mutmut show <mutant_name>` to see the details of a specific mutant (e.g. `mutmut show calculator.x_factorial__mutmut_6`)
This will show exactly what was changed in the code to create the mutant.

- Run 'mutmut browser` to see an interactive HTML report of all the mutants


Also see
* https://about.codecov.io/blog/getting-started-with-mutation-testing-in-python-with-mutmut/
* https://medium.com/@dead-pixel.club/mutation-testing-in-python-using-mutmut-a094ad486050 
 
### <a name='JupyterSetup'></a>Jupyter Setup
This repo is designed so that the Jupyter notebooks can be run from the project root directory. All the dependencies
for Jupyter are listed in `dev-requirements.txt`. All Jupyter notebooks are in the `notebooks/` directory.

- Start up the virtual environment `source .venv/bin/activate`
- Install the dev dependencies `pip install -r dev-requirements.txt`
- The virtual environment needs to be registered with Jupyter so that the notebooks can use the same environment.
```bash
python -m ipykernel install --user --name=hello-python --display-name "Python (hello-python)"
```
- This will create a new kernel named "Python (hello-python)" that you can select from within the Jupyter interface.

- Lauch the Jupyter notebook server - `jupyter notebook`
- Make sure to use the correct kernel. When you create a new notebook (or open an existing one) 
    - Go to the "Kernel" menu
    - Select "Change kernel"
    - Choose **"Python (hello-python)"** from the list.

This ensures your notebook is executing code with the same Python interpreter and packages as the rest of your project.

#### <a name='Usingpackagesineditablemode'></a>Using packages in editable mode
By default, Jupyter notebooks do not reflect changes made to the source code of modules immediately. To enable this, all the modules in this repo must be installed in "editable" mode.

From the project root directory, run
```bash
pip install -e .
```

This command uses the `setup.py` file to install the package, and the `-e` flag (short for `--editable`) creates a symbolic link from your Python environment's `site-packages` directory to your source code.

Even with the package installed in editable mode, Jupyter notebooks will not automatically reload the module every time you make a change. To enable automatic reloading, you need to use the `autoreload` extension.

In a Jupyter notebook cell, run the following commands:

```python
%load_ext autoreload
%autoreload 2
```

- `%load_ext autoreload`: This loads the `autoreload` extension.
- `%autoreload 2`: This sets the `autoreload` mode to automatically reload all modules before executing any code.

#### <a name='nbconvert'></a>nbconvert

The `nbconvert` tool is included with Jupyter and allows you to convert Jupyter notebooks to various formats including Python scripts, HTML, PDF, and Markdown. It also supports executing notebooks and clearing outputs.

- Convert to a python script - `jupyter nbconvert --to script notebooks/app.ipynb`
- Convert to markdown - `jupyter nbconvert --to markdown notebooks/app.ipynb`
- Clear outputs - `jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/app.ipynb`
- Execute and save notebook - `jupyter nbconvert --to notebook --execute --inplace notebooks/app.ipynb`

See https://nbconvert.readthedocs.io/en/latest/ for more details.

## <a name='OtherDeveloperNotes'></a>Other Developer Notes
### <a name='ConfiguretheGituserforthisrepo'></a>Configure the Git user for this repo

- `git config user.email "foo@bar.com"`
- `git config user.namae "John Doe"`

### <a name='SetupSSHkeysforGithub'></a>Setup SSH keys for Github
Need this SSH key to clone and push from github. For obvious reasons we want to set it up to support multiple ssh keys (separate ones for work and personal stuff)

- `cd ~/.ssh` 
- Gen a new SSH key and save it `ssh-keygen -t rsa -C "name@personal_email.com"`
- Save this to a personal file `id_rsa_personal`
- Create a `config` file in `~/.ssh` folder, and put the following lines
```
# Personal account
Host github.com
HostName github.com
IdentityFile ~/.ssh/id_rsa_personal
User git
IdentitiesOnly yes
# Add similar entries for work accounts
```
- Add this ssh key to `github.com`
    - `pbcopy < ~/.ssh/id_rsa_personal.pub`
    - login to `github.com` 
    - Profile Picture -> Settings
    - From Left Sidebar, choose "SSH and GPG Keys"
    - Add "New SSH Key"
    - Paste the key here ...


Resources
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh 
- https://connkat.medium.com/setting-up-multiple-ssh-keys-on-one-computer-75f068d972d9


## <a name='Resources'></a>Resources


## <a name='Scratchpad'></a>Scratchpad

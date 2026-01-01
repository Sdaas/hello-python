
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
* [Usage](#Usage)
* [Developer Setup](#DeveloperSetup)
	* [Python Setup](#PythonSetup)
	* [Visual Code Setup](#VisualCodeSetup)
	* [Setup Pre-Commit Hook to Clear the output of Notebooks](#SetupPre-CommitHooktoCleartheoutputofNotebooks)
	* [Setup the Virtual Environment](#SetuptheVirtualEnvironment)
	* [Installing and managing packages](#Installingandmanagingpackages)
	* [Testing](#Testing)
		* [Logging with Pytest](#LoggingwithPytest)
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


### <a name='Installingandmanagingpackages'></a>Installing and managing dependencies

All dependencies should be listed in `requirements.txt` file. 

- Make sure that the virtual environment is activated.
- Install all dependencies - `pip install -r requirements.txt`
- Install all the developer dependencies - `pip install -r dev-requirements.txt`
- All these dependencies will be installed in the virtual environment.

To install a new package, do the following
- Install the package `pip install xxx`
- Capture the current env into a file `pip freeze > requirements.txt` and check this into git.

FWIW, this entire process can be automated by adding the following snippet in `~/.zshrc`
```zsh
pyinstall() {
    pip install "$@"
    pip freeze > requirements.txt
    echo "Updated requirements.txt with the latest packages."
}
```
Now just run `pyinstall xxx` and the `requirements.txt` file will be updated so you will not forget to commit it.

### Useful Packages
This repo is already setup with some useful packages. Here are some of them

#### pytest

Testing framework. See the section on [Testing](#Testing) for more details on how to use `pytest`.
Also see https://docs.pytest.org/en/7.4.x/

#### python-dotenv

`python-dotenv`  reads key-value pairs from a `.env` file and can set them as environment variables.
- See https://pypi.org/project/python-dotenv/ 
- Don't use dotenv - thats an older and incorrect package
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

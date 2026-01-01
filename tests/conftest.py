# conftest.py
#
# This file is used by pytest to configure the test environment.
# Its primary purpose here is to modify the Python system path (sys.path)
# to ensure that modules in the parent directory (the project root) are
# discoverable by tests located within this 'tests/' directory.
#
# Without this, pytest would not be able to find and import 'app.py'
# when 'tests/test_app.py' tries to do 'from app import add, subtract'.

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

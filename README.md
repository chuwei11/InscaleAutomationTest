## Features

UI automation with Playwright (Python)

Test execution with Pytest

Easy setup with virtual environment

Supports running in headless or headed mode

## Clone the repository

- git clone https://github.com/chuwei11/InscaleAutomationTest.git
- cd InscaleAutomationTest

## Setup VSCode

- Add autocomplete.
  - Install the Python plugin released by Microsoft.

- Allow running the tests by clicking the play icon next to test name.
  - Configure (CMD+Shift+P) `Python: Configure Tests` to pytest.

- Enable debugging so that you can add breakpoints to figure out errors.
  - Install Python Debugger plugin released by Microsoft.

# Install test dependencies

1. Create and activate a virtual environment

- python -m venv venv
- python3 -m venv .venv # if the first one doesnt work
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows


2. Install dependencies
- source .venv/bin/activate
- pip install -r requirements.txt
- playwright install


3. Run tests
- pytest tests/test_add_delete_cust.py
- pytest tests/test_credit_debit_baance.py

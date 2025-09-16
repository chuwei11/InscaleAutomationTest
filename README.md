🔹 Features

UI automation with Playwright (Python)

Test execution with Pytest

Easy setup with virtual environment

Supports running in headless or headed mode

🔹 Setup

1. Clone the repository

- git clone https://github.com/chuwei11/InscaleAutomationTest.git
- cd InscaleAutomationTest


2. Create and activate a virtual environment

- python -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows


3. Install dependencies

- pip install -r requirements.txt
- playwright install


4. Run tests
- pytest tests/test_add_delete_cust.py
- pytest tests/test_credit_debit_baance.py
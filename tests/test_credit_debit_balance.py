from playwright.sync_api import expect
import time

def test_customer_login_select_account(page):
    """
    Test customer login, select account, perform transactions (Credit/Debit),
    and validate that the balance updates correctly.
    """
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    # Customer login as Hermoine Granger
    page.click("button[ng-click='customer()']")
    page.select_option("select#userSelect", label="Hermoine Granger")
    page.click("button[type='submit']")
    assert page.locator(".fontBig").inner_text().strip() == "Hermoine Granger"

    # Select account 1003
    page.select_option("select#accountSelect", label="1003")
    assert page.locator("strong.ng-binding").nth(0).inner_text().strip() == "1003"

    transactions = [
        {"amount": 50000, "type": "Credit"},
        {"amount": 3000, "type": "Debit"},
        {"amount": 2000, "type": "Debit"},
        {"amount": 5000, "type": "Credit"},
        {"amount": 10000, "type": "Debit"},
        {"amount": 15000, "type": "Debit"},
        {"amount": 1500, "type": "Credit"},
    ]

    current_balance = 0

    def perform_transaction(txn_type: str, amount: int):
        # Click appropriate tab
        if txn_type == "Credit":
            page.click("button[ng-click='deposit()']")
        else:
            page.click("button[ng-click='withdrawl()']")

        # Locate input
        amount_input = page.locator("input[ng-model='amount']")
        amount_input.wait_for(state="visible")

        # Retry typing until value is correctly set
        for _ in range(5):
            amount_input.click()
            amount_input.fill("")                # clear old value
            amount_input.type(str(amount), delay=100)
            if amount_input.input_value() == str(amount):
                break
            time.sleep(0.5)  # small wait before retry
        else:
            raise Exception(f"Failed to input amount {amount} after retries")

        # Submit transaction
        if txn_type == "Credit":
            page.click("button.btn.btn-default:has-text('Deposit')")
            expect(page.locator("span.error.ng-binding")).to_have_text("Deposit Successful")
        else:
            page.click("button.btn.btn-default:has-text('Withdraw')")
            expect(page.locator("span.error.ng-binding")).to_have_text("Transaction successful")

    # Loop through all transactions and validate balance
    for txn in transactions:
        perform_transaction(txn["type"], txn["amount"])
        current_balance += txn["amount"] if txn["type"] == "Credit" else -txn["amount"]

        # Validate the updated balance on the UI - check if balance is tally
        balance_display = page.locator("strong.ng-binding").nth(1)
        expect(balance_display).to_have_text(str(current_balance))
        print(f" {txn['type']} {txn['amount']} | Balance = {current_balance}")

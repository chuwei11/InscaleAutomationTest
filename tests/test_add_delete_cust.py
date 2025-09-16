def test_add_customers(page):
    
    # Customers to add
    customers = [
        {"first": "Christopher", "last": "Connely", "postcode": "L789C349"},
        {"first": "Frank", "last": "Christopher", "postcode": "A897N450"},
        {"first": "Christopher", "last": "Minka", "postcode": "M098Q585"},
        {"first": "Connely", "last": "Jackson", "postcode": "L789C349"},
        {"first": "Jackson", "last": "Frank", "postcode": "L789C349"},
        {"first": "Minka", "last": "Jackson", "postcode": "A897N450"},
        {"first": "Jackson", "last": "Connely", "postcode": "L789C349"},
    ]
    
    # Customers to delete
    customers_to_delete = [
        {"first": "Jackson", "last": "Frank", "postcode": "L789C349"},
        {"first": "Christopher", "last": "Connely", "postcode": "L789C349"},
    ]

    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    # Bank Manager Login
    page.click("button[ng-click='manager()']")
    page.click("button[ng-click='addCust()']")

    # Always autoaccept dialogs
    page.on("dialog", lambda dialog: dialog.accept())

    # Looping customers to add
    for cust in customers:
        page.fill("input[ng-model='fName']", cust["first"])
        page.fill("input[ng-model='lName']", cust["last"])
        page.fill("input[ng-model='postCd']", cust["postcode"])
        page.click("button[type='submit']")

    # Navigate to Customers tab and verify if customer table appear
    page.click("button[ng-click='showCust()']")
    page.wait_for_selector("table tbody tr")

    # Verify all customers exist in the table
    for cust in customers:
        row_locator = page.locator("table tbody tr", has_text=cust["first"]).filter(
            has_text=cust["last"]
        ).filter(has_text=cust["postcode"])
        assert row_locator.count() > 0, f"Customer not found: {cust}"
        
    # Delete customers
    for cust in customers_to_delete:
        # Locate the row containing this customer's data
        row = (
            page.locator("table tbody tr", has_text=cust["first"])
            .filter(has_text=cust["last"])
            .filter(has_text=cust["postcode"])
        )

        # Verify if row exist, click on delete button and check if the row is still there
        assert row.count() > 0, f"Customer not found before delete: {cust}"
        row.locator("button", has_text="Delete").click()
        assert (
            row.count() == 0
        ), f"Customer still present after delete: {cust}"

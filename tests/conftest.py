import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Launch a Chromium browser for the whole test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headed mode by default
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Create a new browser page for each test."""
    page = browser.new_page()
    yield page
    page.close()

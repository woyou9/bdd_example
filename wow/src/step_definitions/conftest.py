import pytest
from playwright.sync_api import sync_playwright
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage


@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=750)
        yield browser
        browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(viewport={"width": 1536, "height": 864})
    yield context
    context.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def practice_form_page(page):
    return PracticeFormPage(page)


@pytest.fixture
def navigate_and_login(practice_form_page):
    # login
    practice_form_page.page.goto('https://demoqa.com/automation-practice-form', wait_until='load')

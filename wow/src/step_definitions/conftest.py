import pytest
from playwright.sync_api import sync_playwright
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage
from wow.src.utils.env_vars import FORM_URL

@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
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
    # practice_form_page.login_field.clear()
    # practice_form_page.login_field.fill(login)
    # practice_form_page.password_field.clear()
    # practice_form_page.password_field.clear(password)
    # przykładowy login, ta strona nie ma logowania
    practice_form_page.page.goto(FORM_URL, wait_until='load')

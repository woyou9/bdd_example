import pytest
from playwright.sync_api import sync_playwright
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage


@pytest.fixture
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=0)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture()
def practice_form_page(page):
    return PracticeFormPage(page)


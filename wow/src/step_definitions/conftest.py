import os
import pytest
from playwright.sync_api import sync_playwright
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage
from dotenv import load_dotenv
from wow.src.pages.page_objects.upload_and_download_page import UploadAndDownloadPage


load_dotenv()
FORM_URL = os.environ['FORM_URL']
MODAL_HEADER_TEXT = os.environ['MODAL_HEADER_TEXT']
UPLOAD_AND_DOWNLOAD_URL = os.environ['UPLOAD_AND_DOWNLOAD_URL']


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=0)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context(viewport={"width": 1536, "height": 864})
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def practice_form_page(page):
    return PracticeFormPage(page)


@pytest.fixture(scope="session")
def upload_and_download_page(page):
    return UploadAndDownloadPage(page)


@pytest.fixture
def download_file(browser_context):
    page = browser_context.new_page()
    page.goto(UPLOAD_AND_DOWNLOAD_URL, wait_until='load')
    upload_and_download_page = UploadAndDownloadPage(page)
    with upload_and_download_page.page.expect_download() as download_info:
        upload_and_download_page.download_button.click(force=True)
    download = download_info.value
    path = download.path()
    upload_and_download_page.page.close()
    return path


@pytest.fixture(scope="session")
def navigate_and_login(practice_form_page):
    practice_form_page.page.goto(FORM_URL, wait_until='load')
    return practice_form_page


# analogicznie można zrobić w teście zmienną na poziomie modułu
@pytest.fixture
def shared_context():
    return {}

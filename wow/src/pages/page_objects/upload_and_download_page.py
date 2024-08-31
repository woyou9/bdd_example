from playwright.sync_api import Page
from wow.src.pages.locators.upload_and_download_page_locators import UploadAndDownloadPageLocators


class UploadAndDownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.download_button = self.page.locator(UploadAndDownloadPageLocators.DOWNLOAD_BUTTON)




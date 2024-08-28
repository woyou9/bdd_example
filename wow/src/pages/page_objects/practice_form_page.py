from playwright.sync_api import Page
from wow.src.pages.locators.practice_form_locators import PracticeFormLocators


class PracticeFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input_field = self.page.locator(PracticeFormLocators.FIRST_NAME_INPUT_FIELD)
        self.last_name_input_field = self.page.locator(PracticeFormLocators.LAST_NAME_INPUT_FIELD)
        self.mobile_number_input_field = self.page.locator(PracticeFormLocators.MOBILE_NUMBER_INPUT_FIELD)
        self.gender_radio_buttons = self.page.locator(PracticeFormLocators.GENDER_RADIO_BUTTONS)
        self.submit_button = self.page.locator(PracticeFormLocators.SUBMIT_BUTTON)
        self.thanks_for_submitting_header = self.page.locator(PracticeFormLocators.THANKS_FOR_SUBMITTING_HEADER)

    def fill_name_field(self, first_name):
        self.first_name_input_field.clear()
        self.first_name_input_field.fill(first_name)

    def fill_last_name_field(self, last_name):
        self.last_name_input_field.clear()
        self.last_name_input_field.fill(last_name)

    def fill_mobile_number(self, mobile_number):
        self.mobile_number_input_field.clear()
        self.mobile_number_input_field.fill(mobile_number)


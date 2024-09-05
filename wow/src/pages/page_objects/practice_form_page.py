from playwright.sync_api import Page
from wow.src.pages.locators.practice_form_page_locators import PracticeFormPageLocators


class PracticeFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input_field = self.page.locator(PracticeFormPageLocators.FIRST_NAME_INPUT_FIELD)
        self.last_name_input_field = self.page.locator(PracticeFormPageLocators.LAST_NAME_INPUT_FIELD)
        self.mobile_number_input_field = self.page.locator(PracticeFormPageLocators.MOBILE_NUMBER_INPUT_FIELD)
        self.gender_radio_buttons = self.page.locator(PracticeFormPageLocators.GENDER_RADIO_BUTTONS)
        self.submit_button = self.page.locator(PracticeFormPageLocators.SUBMIT_BUTTON)
        self.thanks_for_submitting_header = self.page.locator(PracticeFormPageLocators.THANKS_FOR_SUBMITTING_HEADER)
        self.upload_file_button = self.page.locator(PracticeFormPageLocators.UPLOAD_FILE_BUTTON)
        self.student_name_table_cell_value = self.page.locator(PracticeFormPageLocators.STUDENT_NAME_TABLE_CELL_VALUE)
        self.mobile_number_table_cell_value = self.page.locator(PracticeFormPageLocators.MOBILE_NUMBER_TABLE_CELL_VALUE)
        self.gender_table_cell_value = self.page.locator(PracticeFormPageLocators.GENDER_TABLE_CELL_VALUE)
        self.close_summary_modal_button = self.page.locator(PracticeFormPageLocators.CLOSE_SUMMARY_MODAL_BUTTON)
        self.picture_name_table_cell_value = self.page.locator(PracticeFormPageLocators.PICTURE_NAME_TABLE_CELL_VALUE)
        self.summary_form_table = self.page.locator(PracticeFormPageLocators.SUMMARY_FORM_TABLE)
        self.form_header = self.page.locator(PracticeFormPageLocators.FORM_HEADER)

    def fill_name_field(self, first_name):
        self.first_name_input_field.clear()
        self.first_name_input_field.fill(first_name)

    def fill_last_name_field(self, last_name):
        self.last_name_input_field.clear()
        self.last_name_input_field.fill(last_name)

    def fill_mobile_number(self, mobile_number):
        self.mobile_number_input_field.clear()
        self.mobile_number_input_field.fill(mobile_number)

    def upload_profile_picture(self, file_path):
        with self.page.expect_file_chooser() as fc_info:
            self.upload_file_button.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)


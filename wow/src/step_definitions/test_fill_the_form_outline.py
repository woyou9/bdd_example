import pytest
from playwright.sync_api import expect
from pytest_bdd import scenario, scenarios, when, then, given, parsers
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage
from wow.src.step_definitions.conftest import MODAL_HEADER_TEXT


@pytest.mark.outline_scenario_usage
@scenario('../features/submit_form_outline.feature', 'Fill all the required fields and then submit the form')
def test_form_with_outline():
    pass


@given(parsers.parse('the user is on the practice form page'))
def go_to_practice_form(navigate_and_login):
    pass


@when(parsers.parse('the user fills "{first_name}" in the required first name field'))
def fill_required_name_field(practice_form_page: PracticeFormPage, first_name):
    practice_form_page.fill_name_field(first_name)


@when(parsers.parse('the user fills "{last_name}" in the required last name field'))
def fill_required_last_name_field(practice_form_page: PracticeFormPage, last_name):
    practice_form_page.fill_last_name_field(last_name)


@when(parsers.parse('the user selects {gender} gender radio button'))
def select_gender(practice_form_page: PracticeFormPage, gender):
    practice_form_page.page.locator(f'.custom-radio [value={gender}]').click(force=True)


@when(parsers.parse('the user fills "{mobile_number}" in the required mobile number field'))
def fill_required_last_name_field(practice_form_page: PracticeFormPage, mobile_number):
    practice_form_page.fill_mobile_number(mobile_number)


@when(parsers.parse('the user uploads profile picture file'))
def upload_picture(download_file, practice_form_page: PracticeFormPage):
    file_name = download_file
    practice_form_page.upload_profile_picture(file_name)


@when(parsers.parse('the user presses submit button'))
def press_submit(practice_form_page: PracticeFormPage):
    practice_form_page.submit_button.click()


@then(parsers.parse('the modal window with form summary should be visible'))
def check_for_modal_window_header(practice_form_page: PracticeFormPage):
    expect(practice_form_page.thanks_for_submitting_header).to_be_visible()
    expect(practice_form_page.thanks_for_submitting_header).to_contain_text(MODAL_HEADER_TEXT)


@then(parsers.parse('the form summary should contain filled fields such as "{first_name}", "{last_name}", "{mobile_number}" and "{gender}"'))
def assert_values_in_form_summary(practice_form_page: PracticeFormPage, first_name, last_name, mobile_number, gender):
    expect(practice_form_page.student_name_table_cell_value).to_contain_text(f'{first_name} {last_name}')
    expect(practice_form_page.mobile_number_table_cell_value).to_contain_text(mobile_number)
    expect(practice_form_page.gender_table_cell_value).to_contain_text(gender)
    practice_form_page.page.locator('#closeLargeModal').click()
    # practice_form_page.page.reload()

import pytest
from playwright.sync_api import expect
from pytest_bdd import scenario, scenarios, when, then, given, parsers
from wow.src.pages.page_objects.practice_form_page import PracticeFormPage
from wow.src.step_definitions.conftest import practice_form_page

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


@when(parsers.parse('the user selects gender radio button'))
def select_gender(practice_form_page: PracticeFormPage):
    practice_form_page.gender_radio_buttons.first.click()


@when(parsers.parse('the user fills "{mobile_number}" in the required mobile number field'))
def fill_required_last_name_field(practice_form_page: PracticeFormPage, mobile_number):
    practice_form_page.fill_mobile_number(mobile_number)


@when(parsers.parse('the user presses submit button'))
def press_submit(practice_form_page: PracticeFormPage):
    practice_form_page.submit_button.click()


@then(parsers.parse('the modal window with form summary should be visible'))
def check_for_modal_window_header(practice_form_page: PracticeFormPage):
    expect(practice_form_page.thanks_for_submitting_header).to_be_visible()

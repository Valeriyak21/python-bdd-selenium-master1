from behave import *
from hamcrest import *

# noinspection PyUnresolvedReferences
from utilities.config import Config

use_step_matcher('re')

@when("I click Администрирование page")
def search_button(context):
    context.main_page.click_admin_page()

@When("I click Диалоги page")
def search_dialogs(context):
    context.main_page.click_dialogs_page()

@When("I click Search button")
def search_dialogs(context):
    context.main_page.click_search()

@When("I enter '(.*)' Search field")
def search_dialogs(context, text):
    context.main_page. enter_text(text)

@When("I click notifications button")
def search_dialogs(context):
    context.main_page.click_notifications()

@When("I click write button")
def search_dialogs(context):
    context.main_page.click_write_button()

@Then("I click my lenta page")
def search_dialogs(context):
    context.main_page.click_my_lenta_page()

@Then("I click write")
def click_write(context):
    context.main_page.click_write()

@Then("I click development page")
def click_write(context):
    context.main_page.click_dev_page()

@When("I click streams page")
def click_write(context):
    context.main_page.click_page_streams()

@When("I click hab page")
def click_write(context):
    context.main_page.click_page_hab()

@When("I click information security page")
def click_write(context):
    context.main_page.click_page_infb()

@When("I click log out")
def click_write(context):
    context.main_page. click_logout()




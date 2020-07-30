from behave import *
from hamcrest import *

# noinspection PyUnresolvedReferences
from utilities.config import Config

use_step_matcher('re')

@given("I open Habr URL in browser")
def open_github(context):
    context.main_page.open(Config.APP_URL_1)

@when("I click Войти button")
def search_button(context):
    context.main_page.click_button_login()

@when("I enter '(.*)' login")
def search_login(context, text):
    context.main_page.submit_login(text)

@when("I enter '(.*)' password")
def search_password(context, text):
        context.main_page.submit_password(text)

@when("I click Войти")
def search_button(context):
    context.main_page.click_login()

@Then("I click account")
def search_button(context):
    context.main_page.click_button_account()

@Then("I get name account")
def account_name(context):
   context.main_page.account_name()





from behave import *


@given('i am an e-pneu user')
def step_impl(context):
    context.homePage.site_acces()


@when('i type in search field')
def step_impl(context):
    context.homePage.search_field()


@when('i search for tires')
def step_impl(context):
    context.homePage.search_btn()


@when('i click on logo')
def step_impl(context):
    context.homePage.logo_click()


@then('i return to homepage')
def step_impl(context):
    context.homePage.homepage_link_check()
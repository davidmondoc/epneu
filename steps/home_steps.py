from behave import *


@given ('i am an e-pneu user')
def step_impl(context):
    context.Home_page.site_acces()


@when( 'i click on logo')
def step_impl(context):
    context.Home_page.logo_click()


@then('i return to homepage')
def step_impl(context):
    context.Home_page.homepage_link_check()
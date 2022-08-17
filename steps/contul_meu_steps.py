from behave import *

@given('i am trying to login to my account')
def step_impl(context):
    context.contulMeu.site_acces()


@when('i navigate to account login')
def step_impl(context):
    context.contulMeu.account_page()


@when('i type in my email')
def step_impl(context):
    context.contulMeu.user()


@when('i type in my password')
def step_impl(context):
    context.contulMeu.password()


@when('i forgot my password')
def step_impl(context):
    context.contulMeu.forgot_pass()


@when('i return to my account page')
def step_impl(context):
    context.contulMeu.go_back()


@when('i press autentificare')
def step_impl(context):
    context.contulMeu.autentificare()


@then('i check if error message is displayed on password field')
def step_impl(context):
    context.contulMeu.errormsg()

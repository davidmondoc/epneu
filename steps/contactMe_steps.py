from behave import *

@given('i want to be contacted')
def step_impl(context):
    context.contactMe.site_acces()

@when('i click on contact me button')
def step_impl(context):
    context.contactMe.contact_btn()

@when('i type in my name')
def step_impl(context):
    context.contactMe.input_name()

@when('i type in my phone no.')
def step_impl(context):
    context.contactMe.input_phone()

@when('i type in my email adress')
def step_impl(context):
    context.contactMe.input_mail()

@then('i send request')
def step_impl(context):
    context.contactMe.click_send()
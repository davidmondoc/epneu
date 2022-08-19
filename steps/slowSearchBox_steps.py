from behave import *


@given('i am using another methode to search for tires')
def step_impl(context):
    context.ssb.site_acces()


@when('i click on tire type')
def step_impl(context):
    context.ssb.tiretype_src()


@when('i click on width selection')
def step_impl(context):
    context.ssb.tirewidth()


@then('i initiate search')
def step_impl(context):
    context.ssb.clicksrc()


from behave import *


@given('i am using another methode to search for tires')
def step_impl(context):
    context.ssb.site_acces()


@when('i click on tire type')
def step_impl(context):
    context.ssb.tiretype_src()


@when('i click on width selection')
def step_impl(context):
    context.ssb.width()


@when('i click on height selection')
def step_impl(context):
    context.ssb.height()


@when('i click on diameter selection')
def step_impl(context):
    context.ssb.diameter()


@when('i click on season selection')
def step_impl(context):
    context.ssb.season()


@when('i click on producer selection')
def step_impl(context):
    context.ssb.producer()

@then('i initiate search')
def step_impl(context):
    context.ssb.clicksrc()


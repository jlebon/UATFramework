'''test methods for dummy features'''

from behave import *

@given('this is a dummy condition')
def step_impl(context):
	pass

@then('this is a dummy success')
def step_impl(context):
	assert True

@then('this is a dummy failure')
def step_impl(context):
	assert False

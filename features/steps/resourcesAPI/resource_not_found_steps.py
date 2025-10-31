from behave import then

@then('the response has returned empty with no body')
def step_empty_response(context):
    assert context.response.content in (b'{}', None), f"Response is not empty"

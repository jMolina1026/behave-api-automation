from behave import then

@then('the response returned has not content')
def step_check_no_content(context):
    body = context.response.text.strip()
    assert body == "", f"Expected empty body for 204 response, but got: {body!r}"

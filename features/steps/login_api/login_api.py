from behave import then


@then('the user has logged in successfully and a {key} is generated')
def step_login_success(context, key):
    response_body = context.response.json()
    print(response_body.keys())
    assert key in response_body.keys(), f"{key} not found in response"


@then('the Login user response body has a key with a value: {key} = "{value}"')
def step_check_property_value(context, key, value):
    response_body: object = context.response.json()
    assert key in response_body, f"Missing key '{key}' in response body"
    assert response_body[key] == value, f"Incorrect value for key '{key}' in response body"
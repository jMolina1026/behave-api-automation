from behave import then
from pydantic import ValidationError

from features.schemas.register_user_schema import RegisterUser, RegisterUserUnsuccessful


@then('the datatypes are correct for a POST registered user: {schema}')
def step_register_user_success(context, schema):
    schema_map = {
        "RegisterUser": RegisterUser,
        "RegisterUserUnsuccessful": RegisterUserUnsuccessful
    }
    json_data = context.response.json()
    try:
        schema_map.get(schema)(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"


@then('the POST register user response body should contain the new attributes from the request body')
def step_validate_response(context):
    request_body: object = context.request_body
    response_body: object = context.response.json()
    print(f"request_body: {request_body}")
    print(f"response_body: {response_body}")
    for key, value in request_body.items():
        assert key in response_body, f"Missing key '{key}' in response body"
        assert response_body[key] == value, \
            f"For key '{key}', expected '{value}' but got '{response_body[key]}'"


@then('every item in POST Register User response should have the expected {keys}')
def step_check_property(context, keys):
    expected_keys: set = {k.strip() for k in keys.split(',') if k.strip()}
    prop_key: set = set(context.response.json().keys())

    # print(f"expected_keys: {expected_keys}")
    # print(f"prop_key: {prop_key}")

    # Check all expected keys are present
    missing = expected_keys - prop_key
    assert not missing, f"Missing keys: {missing}"

    # Check for unexpected extra keys
    extra = prop_key - expected_keys
    assert not extra, f"Unexpected keys found: {extra}"


@then('the Register user response body has a key with a value: {key} = "{value}"')
def step_check_property_value(context, key, value):
    response_body: object = context.response.json()
    assert key in response_body, f"Missing key '{key}' in response body"
    assert response_body[key] == value, f"Incorrect value for key '{response_body[key]}' in response body"
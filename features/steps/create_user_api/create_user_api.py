from behave import then
from pydantic import BaseModel, ValidationError

from features.schemas.created_user_schemas import CreatedUser
import logging
logging.basicConfig(level=logging.INFO)

@then('the POST create user response returns property key "{key}": {expected_value}')
def step_check_property(context, key, expected_value):
    # json_data = context.response.json()
    # respkey = json_data[f'{key}']
    assert context.response.json() == int(expected_value), f"Expected '{key}' to have value = {expected_value} but got value = {context.response.json()}"


@then('every item in User Creation response should have the expected {keys}')
def step_check_keys(context, keys):
    expected_keys = {k.strip() for k in keys.split(",") if k.strip()} # a set
    prop_key = set(context.response.json().keys())

    # Check all expected keys are present
    missing = expected_keys - prop_key
    assert not missing, f"Missing keys: {missing}"

    # Check for unexpected extra keys
    extra = prop_key - expected_keys
    assert not extra, f"Unexpected keys found: {extra}"


@then('the datatypes are correct for a newly Created User')
def step_validate_schema(context):
    json_data = context.response.json()
    try:
        CreatedUser(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"


@then('the response body should contain the new attributes from the request body')
def step_validate_response(context):
    request_body = context.request_body
    response_body = context.response.json()
    print(f"request_body: {request_body}")
    print(f"response_body: {response_body}")
    for key, value in request_body.items():
        assert key in response_body, f"Missing key '{key}' in response body"
        assert response_body[key] == value, \
            f"For key '{key}', expected '{value}' but got '{response_body[key]}'"



@then('the response body should contain the extra fields in addition to the request body, extra fields: {keys}')
def step_validate_response(context, keys):
    response_body = context.response.json()
    extra_keys = {k.strip() for k in keys.split(",") if k.strip()}
    for extra_key in extra_keys:
        assert extra_key in response_body, f"Expected field '{extra_key}' in response, but only got {response_body.keys()}"

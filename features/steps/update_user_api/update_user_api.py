from behave import then
from pydantic import ValidationError

from features.schemas.update_user_schemas import UpdateUserSchema


@then('every item in Update User response should ave the expected {keys} items')
def step_check_property(context, keys):
    expected_keys = {k.strip() for k in keys.split(',') if k.strip()}
    prop_key = set(context.response.json().keys())

    # Check all expected keys are present
    missing = expected_keys - prop_key
    assert not missing, f"Missing keys: {missing}"

    # Check for unexpected extra keys
    extra = prop_key - expected_keys
    assert not extra, f"Unexpected keys found: {extra}"

@then('the datatypes are correct for an updated User: {schema}')
def step_validate_schema(context, schema):
    schema_map = {
        "UpdateUserSchema": UpdateUserSchema,
    }
    json_data = context.response.json()
    try:
        schema_map.get(schema)(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"


@then('the PUT update user response body should contain the new attributes from the request body')
def step_validate_response(context):
    request_body = context.request_body
    response_body = context.response.json()
    print(f"request_body: {request_body}")
    print(f"response_body: {response_body}")
    for key, value in request_body.items():
        assert key in response_body, f"Missing key '{key}' in response body"
        assert response_body[key] == value, \
            f"For key '{key}', expected '{value}' but got '{response_body[key]}'"


@then('the PUT update user response body should contain the extra fields in addition to the request body, extra fields: {keys}')
def step_validate_response(context, keys):
    response_body = context.response.json()
    extra_keys = {k.strip() for k in keys.split(",") if k.strip()}
    for extra_key in extra_keys:
        assert extra_key in response_body, f"Expected field '{extra_key}' in response, but only got {response_body.keys()}"
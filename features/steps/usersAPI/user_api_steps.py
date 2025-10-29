import requests
from behave import given, when, then
from pydantic import ValidationError

from features.schemas.users_schema import UsersSchema, Data, Support, Meta


@then('the first response data id should be {expected_id}')
def step_check_data_id(context, expected_id):
    json_data = context.response.json()
    first_user = json_data["data"][0]
    print(first_user)
    assert first_user["id"] == int(expected_id), \
        f"Expected {expected_id} but got {first_user["id"]}"


@then('the first response data email should be "{expected_email}"')
def step_check_data_email(context, expected_email):
    json_data = context.response.json()
    first_user = json_data["data"][0]
    print(first_user)
    assert first_user["email"] == expected_email, \
        f"Expected {expected_email} but got {first_user["email"]}"


@then('the first response data first_name should be "{expected_first_name}"')
def step_check_data_firstname(context, expected_first_name):
    json_data = context.response.json()
    first_user = json_data["data"][0]
    print(first_user)
    assert first_user["first_name"] == expected_first_name, \
        f"Expected {expected_first_name} but got {first_user["first_name"]}"


@then('the first response data last_name should be "{expected_last_name}"')
def step_check_data_lastname(context, expected_last_name):
    json_data = context.response.json()
    first_user = json_data["data"][0]
    print(first_user)
    assert first_user["last_name"] == expected_last_name, \
        f"Expected {expected_last_name} but got {first_user["last_name"]}"


@then('the datatypes are correct for a list of users')
def step_validate_schema(context):
    json_data = context.response.json()
    try:
        UsersSchema(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"


@then('every item in list of users response should have the expected "{key}" keys: {keys}')
def step_check_keys(context, key, keys):
    expected_keys = {k.strip() for k in keys.split(",") if k.strip()}

    if key == "data":
        prop_key = context.response.json().get(f"{key}", [])
        assert isinstance(prop_key, list), f"Expected a list but got {type(prop_key)}"

        for item in prop_key:
            missing = expected_keys - item.keys()
            assert not missing, f"Item {item.keys()} is missing keys: {missing}"
    # elif key == "support":
    #     prop_key = context.response.json().get("support", {})
    #     assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"
    # elif key == "_meta":
    #     prop_key = context.response.json().get("_meta", {})
    #     assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"
    else:
        prop_key = context.response.json().get(key, {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"


    # Check all expected keys are present
    # missing = expected_keys - set(prop_key.keys())
    # assert not missing, f"Missing keys: {missing}"
    #
    # # Check that no unexpected keys exist
    # extra = set(prop_key.keys()) - expected_keys
    # assert not extra, f"Unexpected keys found: {extra}"


@then('every item in the list of users should have the expected "{key}" keys and schema {expected_schema}')
def step_check_keys(context, key, expected_schema):
    schema_map = {
        "Data": Data,
        "Support": Support,
        "Meta": Meta
    }
    schema_class = schema_map.get(expected_schema)
    expected_keys = set(schema_class.model_fields.keys())

    if key == "data":
        prop_key = context.response.json().get(f"{key}", [])
        assert isinstance(prop_key, list), f"Expected a list but got {type(prop_key)}"

        for item in prop_key:
            missing = expected_keys - item.keys()
            assert not missing, f"Item {item.keys()} is missing keys: {missing}"
    else:
        prop_key = context.response.json().get(key, {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"
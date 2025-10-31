from behave import then
from pydantic import BaseModel, ValidationError

from features.schemas.resource_schemas import ResourcesSchema, Data, Support, Meta


@then('the response returns property key "{key}": {expected_value}')
def step_check_property(context, key, expected_value):
    json_data = context.response.json()
    respkey = json_data[f'{key}']
    assert respkey == int(expected_value), f"Expected '{key}' to have value = {expected_value} but got value = {respkey}"


@then('the response returns parent_keys "{parent_key}" with childKey "{key}": {expected_value}')
def step_check_inner_properties(context, parent_key, key, expected_value):
    json_data = context.response.json()
    resp_key = json_data[f'{parent_key}'][0][f'{key}']
    print(resp_key)
    assert resp_key == int(expected_value), f"Expected '{key}' to have value = {expected_value} but got value = {resp_key}"


@then('the response returns parent_keys "{parent_key}" with child_key "{key}": "{expected_string_value}"')
def step_check_inner_properties(context, parent_key, key, expected_string_value):
    json_data = context.response.json()
    resp_key = json_data[f'{parent_key}'][0][f'{key}']
    print(resp_key)
    assert resp_key == expected_string_value, f"Expected '{key}' to have value = {expected_string_value} but got value = {resp_key}"


@then('the count of "{key}" properties should be {expected_count}')
def step_check_count_of_properties(context, key, expected_count):
    json_data = context.response.json()
    resp_count = len(json_data[f'{key}'])
    assert resp_count == int(expected_count), f"Expected '{key}' to have a count = {expected_count} but got a count = {resp_count}"


@then('every item in the response should have the expected "{key}" keys: {keys}')
def step_check_keys(context, key, keys):
    # expected_keys = {"id", "name", "year", "color", "pantone_value"}
    expected_keys = {k.strip() for k in keys.split(",") if k.strip()}

    prop_key = "None"
    if key == "data":
        prop_key = context.response.json().get("data", [])
        assert isinstance(prop_key, list), f"Expected a list but got {type(prop_key)}"

        for item in prop_key:
            missing = expected_keys - item.keys()
            assert not missing, f"Item {item.keys()} is missing keys: {missing}"
    elif key == "support":
        prop_key = context.response.json().get("support", {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"
    elif key == "_meta":
        prop_key = context.response.json().get("_meta", {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"


@then('every item in the response should have the expected "{key}" keys and schema {expected_schema}')
def step_check_keys(context, key, expected_schema):
    schema_map = {
        "Data": Data,
        "Support": Support,
        "Meta": Meta
    }
    schema_class = schema_map.get(expected_schema)
    expected_keys = set(schema_class.model_fields.keys())

    prop_key = "None"
    if key == "data":
        prop_key = context.response.json().get(f"{key}", [])
        assert isinstance(prop_key, list), f"Expected a list but got {type(prop_key)}"

        for item in prop_key:
            missing = expected_keys - item.keys()
            assert not missing, f"Item {item.keys()} is missing keys: {missing}"
    elif key == "support":
        prop_key = context.response.json().get("support", {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"
    elif key == "_meta":
        prop_key = context.response.json().get("_meta", {})
        assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"


@then('the count of "{key}" child properties should be {expected_count}')
def step_check_count_of_properties(context, key, expected_count):
    json_data = context.response.json()

    resp_count = 0
    if key == "data":
        resp_count = len(json_data[f'{key}'][0])
    elif key == "support":
        resp_count = len(json_data[f'{key}'])
    elif key == "_meta":
        resp_count = len(json_data[f'{key}'])
    assert resp_count == int(expected_count), f"Expected '{key}' to have a child property count = {expected_count} but got a count = {resp_count}"


@then('the datatypes are correct')
def step_validate_schema(context):
    json_data = context.response.json()
    try:
        ResourcesSchema(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"

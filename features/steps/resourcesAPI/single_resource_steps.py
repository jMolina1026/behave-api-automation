from behave import then
from pydantic import ValidationError

from features.schemas.resource_schemas import SingleResourceResponse, Data, Support, Meta


@then('the data types are correct for a single resource')
def step_verify_data_schema(context):
    """
    Verify that the data types are correct for a single resource
    :param context: context is an instance of Behave’s Context class, automatically passed into every step, hook, and fixture.
    think of it  as a means of retaining all the info from the response that was just returned for a single test
    :return:
    """
    json_data = context.response.json()
    try:
        SingleResourceResponse(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"


@then('every item in the single resource response should have the expected "{key}" keys: {keys}')
def step_check_keys(context, key, keys):
    expected_keys = {k.strip() for k in keys.split(",") if k.strip()}

    prop_key = context.response.json().get(f"{key}", {})
    assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"

    # Check all expected keys are present
    missing = expected_keys - set(prop_key.keys())
    assert not missing, f"Missing keys: {missing}"

    # Check that no unexpected keys exist
    extra = set(prop_key.keys()) - expected_keys
    assert not extra, f"Unexpected keys found: {extra}"


@then('every item in the single resource response should have the expected "{key}" keys and schema {expected_schema}')
def step_check_keys(context, key, expected_schema):
    schema_map = {
        "Data": Data,
        "Support": Support,
        "Meta": Meta
    }
    schema_class = schema_map.get(expected_schema)
    expected_keys = set(schema_class.model_fields.keys())

    prop_key = context.response.json().get(f"{key}", {})
    assert isinstance(prop_key, dict), f"Expected a dictionary but got {type(prop_key)}"

    # Check all expected keys are present
    missing = expected_keys - set(prop_key.keys())
    assert not missing, f"Missing keys: {missing}"


@then('the count of "{key}" properties for a single resource should be {expected_count}')
def step_check_count_of_properties(context, key, expected_count):
    json_data = context.response.json()
    resp_count = len(json_data[f'{key}'])
    assert resp_count == int(expected_count), f"Expected '{key}' to have a child property count = {expected_count} but got a count = {resp_count}"
from behave import then
import time

from pydantic import ValidationError

from features.schemas.users_schema import UsersSchema


@then("the delayed response after {delay} seconds and {retry} retries, has a response body returned")
def step_impl(context, delay, retry):
    for attempt in range(1, int(retry) + 1):
        if context.response.status_code == 200:
            return context.response
        print(f"Attempt {attempt}: got {context.response.status_code}, retrying in {delay}s...")
        time.sleep(delay)
    raise AssertionError(f"Did not receive 200 after {int(retry) + 1} attempts.")


@then('the datatypes are correct for a delayed response')
def step_validate_schema(context):
    json_data = context.response.json()
    try:
        UsersSchema(**json_data)
    except ValidationError as e:
        assert False, f"Expected a validation error: {e}"

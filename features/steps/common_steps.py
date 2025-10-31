import json

import requests
from behave import given, when, then


@given('the API base URL is "{base_url}"')
def step_set_base_url(context, base_url):
    context.base_url = base_url
    # context.headers = {
    #     "Content-Type": "application/json",
    #     "x-api-key": "reqres-free-v1"
    # }


@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.response = requests.get(url, headers=context.headers)
    print(context.response)


@when('I send a POST request to "{endpoint}" with body')
def step_send_post_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    print(url)
    context.request_body = json.loads(context.text)
    context.response = requests.post(
        url,
        headers=context.headers,
        json = context.request_body,
        proxies = {"http": None, "https": None}
    )


@when('I send a PUT request to "{endpoint}" with body')
def step_send_put_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.request_body = json.loads(context.text)
    context.response = requests.put(url,
        headers=context.headers,
        json=context.request_body
        )


@when('I send a PATCH request to "{endpoint}" with body')
def step_send_put_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.request_body = json.loads(context.text)
    context.response = requests.patch(url,
                                      headers=context.headers,
                                      json=context.request_body
                                      )

@when('I send a DELETE request to "{endpoint}"')
def step_send_delete_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.response = requests.delete(url, headers=context.headers)


@then('the response status code should be {status_code:d}')
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code} but got {context.response.status_code}"


@then('the response status reason should be "{reason}"')
def step_check_response(context, reason):
    assert context.response.reason == reason, \
        f"Expected {reason} but got {context.response.reason}"


@then('the response should contain "{key}"')
def step_check_response_key(context, key):
    json_data = context.response.json()
    print(json_data)
    assert key in json_data, f"Key '{key}' not found in response: {json_data}"

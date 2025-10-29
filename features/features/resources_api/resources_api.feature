@resources
Feature: Resources API
  Tests the resource api

  Scenario: GET the list of resources
#    Given the API base URL is "https://reqres.in/api"
    When I send a GET request to "/unknown"
    Then the response status code should be 200
    And the response returns property key "page": 1
    And the response returns property key "per_page": 6
    And the response should contain "data"
    And the count of "data" properties should be 6
    And the count of "support" properties should be 2
    And the count of "_meta" properties should be 7


  Scenario: GET the list of resources data details
    When I send a GET request to "/unknown"
    Then every item in the response should have the expected "data" keys: id, name, year, color, pantone_value
    Then every item in the response should have the expected "data" keys and schema Data
    And the count of "data" child properties should be 5
    And the response returns parent_keys "data" with childKey "id": 1
    And the response returns parent_keys "data" with child_key "name": "cerulean"


  Scenario: GET the list of resources support details
    When I send a GET request to "/unknown"
    Then every item in the response should have the expected "support" keys: url, text
    And every item in the response should have the expected "support" keys and schema Support
    And the count of "support" child properties should be 2

  Scenario: GET the list of resources _meta details
    When I send a GET request to "/unknown"
    Then every item in the response should have the expected "_meta" keys: powered_by, upgrade_url, docs_url, template_gallery, message, features, upgrade_cta
    And every item in the response should have the expected "_meta" keys and schema Meta
    And the count of "_meta" child properties should be 7

  Scenario: GET and verify the data types
    When I send a GET request to "/unknown"
    Then the datatypes are correct

@resources @single_resource
Feature: Single Resource API
  Testing the single resource API

  Scenario: GET a single Resource
    When I send a GET request to "/unknown/2"
    Then the response status code should be 200


  Scenario: GET and Verify data types
    When I send a GET request to "/unknown/2"
    Then the data types are correct for a single resource


  Scenario: GET a single resource data details
    When I send a GET request to "/unknown/2"
    Then every item in the single resource response should have the expected "data" keys: id, name, year, color, pantone_value
    And every item in the single resource response should have the expected "data" keys and schema Data
    And the count of "data" properties for a single resource should be 5


  Scenario: GET a single resource Support details
    When I send a GET request to "/unknown/2"
    Then every item in the single resource response should have the expected "support" keys: url, text
    And every item in the single resource response should have the expected "support" keys and schema Support
    And the count of "support" properties for a single resource should be 2


  Scenario: GET a single resource data details
    When I send a GET request to "/unknown/2"
    Then every item in the single resource response should have the expected "_meta" keys: powered_by, upgrade_url, docs_url, template_gallery, message, features, upgrade_cta
    And every item in the single resource response should have the expected "_meta" keys and schema Meta
    And the count of "_meta" properties for a single resource should be 7

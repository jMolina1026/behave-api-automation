@resources @no_resource_found
Feature: Resource Not Found API
  Testing a not found resource API

  Scenario: GET a Resource that is Not Found
    When I send a GET request to "/unknown/23"
    Then the response status code should be 404
    And the response has returned empty with no body

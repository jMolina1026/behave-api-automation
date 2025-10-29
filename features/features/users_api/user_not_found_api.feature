@Users @User_not_found
Feature: User Not Found API
  Testing a not found user API

  Scenario: GET a Resource that is Not Found
    When I send a GET request to "/users/23"
    Then the response status code should be 404
    And the user not found response has returned empty with no body
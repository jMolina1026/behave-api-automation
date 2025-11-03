Feature: Delayed Responses

  Scenario: Delayed Responses
    When I send a GET request to "/users?delay=3"
    Then the delayed response after 3 seconds and 5 retries, has a response body returned
    And the datatypes are correct for a delayed response
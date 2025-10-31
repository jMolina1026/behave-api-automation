Feature: Delete a user

  Scenario: DELETE the user
    When I send a DELETE request to "/users/2"
    Then the response status code should be 204
    And the response status reason should be "No Content"
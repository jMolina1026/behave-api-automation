Feature: Login Users

  Scenario: Login Users successfully
    When I send a POST request to "/login" with body
      """
        {
          "email": "eve.holt@reqres.in",
          "password": "cityslicka"
        }
      """
    Then the response status code should be 200
    And the response status reason should be "OK"
    And the user has logged in successfully and a token is generated


  Scenario: Login Users Unsuccessfully
    When I send a POST request to "/login" with body
      """
        {
          "email": "peter@klaven"
        }
      """
    Then the response status code should be 400
    And the response status reason should be "Bad Request"
    And the Login user response body has a key with a value: error = "Missing password"
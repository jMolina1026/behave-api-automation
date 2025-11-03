Feature: POST Register User

  Scenario: POST Register User Unsuccessfully
    When I send a POST request to "/register" with body
      """
        {
          "email": "eve.holt@reqres.in"
        }
      """
    Then the response status code should be 400
    And the response status reason should be "Bad Request"
    Then the Register user response body has a key with a value: error = "Missing password"


  Scenario: POST and Verify the datatypes are correct for a Unsuccessfully registered user
      When I send a POST request to "/register" with body
      """
        {
          "password": "pistol"
        }
      """
      Then the datatypes are correct for a POST registered user: RegisterUserUnsuccessful
      Then every item in POST Register User response should have the expected error
      Then the Register user response body has a key with a value: error = "Missing email or username"

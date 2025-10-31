Feature: POST Register User

  Scenario: POST Register User Successfully
    When I send a POST request to "/register" with body
      """
        {
          "email": "eve.holt@reqres.in",
          "password": "pistol"
        }
      """
    Then the response status code should be 200
    And the response status reason should be "OK"


  Scenario: POST and Verify the datatypes are correct for a successfully registered user
      When I send a POST request to "/register" with body
      """
        {
          "email": "eve.holt@reqres.in",
          "password": "pistol"
        }
      """
      Then the datatypes are correct for a POST successfully registered user: RegisterUser


    Scenario: PATCH and Verify that the Request Body was returned in the Response Body
    When I send a POST request to "/register" with body
      """
        {
          "email": "eve.holt@reqres.in",
          "password": "pistol"
        }
      """
    Then every item in POST Register User response should have the expected token, id

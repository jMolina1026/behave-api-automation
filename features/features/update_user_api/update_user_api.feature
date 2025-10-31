@updateUser
Feature: Update an existing User

  Scenario: PUT updates existing user
    When I send a PUT request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the response status code should be 200
    And every item in Update User response should ave the expected name, job, updatedAt items


  Scenario:  POST and Verify data types for a newly Created User
    When I send a PUT request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the datatypes are correct for an updated User: UpdateUserSchema


  Scenario: PUT and Verify that the Request Body was returned in the Response Body
    When I send a PUT request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the PUT update user response body should contain the new attributes from the request body
    And the PUT update user response body should contain the extra fields in addition to the request body, extra fields: updatedAt

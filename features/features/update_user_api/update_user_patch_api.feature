@updateUser
Feature: Update an existing User using the Patch method

  Scenario: PATCH updates existing user
    When I send a PATCH request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the response status code should be 200
    And every item in Update User response should ave the expected name, job, updatedAt items


  Scenario:  PATCH and Verify data types for a newly Created User
    When I send a PATCH request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the datatypes are correct for a PATCH updated User: UpdateUserPatchSchema


  Scenario: PATCH and Verify that the Request Body was returned in the Response Body
    When I send a PATCH request to "/users/2" with body
      """
        {
          "name": "Joseph",
          "job": "Tester"
        }
      """
    Then the PATCH update user response body should contain the new attributes from the request body
    And the PATCH update user response body should contain the extra fields in addition to the request body, extra fields: updatedAt

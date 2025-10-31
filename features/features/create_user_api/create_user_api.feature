Feature: Create a new user

  Scenario: Creates a new user
    When I send a POST request to "/users" with body
      """
          {
            "name": "Joe",
            "job": "Dirt"
          }
      """
    Then the response status code should be 201
    And every item in User Creation response should have the expected name, job, id, createdAt


  Scenario: POST and Verify that the Request Body was returned in the Response Body
    When I send a POST request to "/users" with body
      """
        {
          "name": "Jane",
          "job": "Mudd"
        }
      """
    Then the response body should contain the new attributes from the request body
    And the response body should contain the extra fields in addition to the request body, extra fields: id, createdAt
    
    
  Scenario: POST and Verify data types for a newly Created User
    When I send a POST request to "/Users" with body
      """
        {
          "name": "Jim",
          "job": "Beam"
        }
      """
    Then the datatypes are correct for a newly Created User

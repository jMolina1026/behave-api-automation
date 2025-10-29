@Users @UserList
Feature:  User API

  Scenario: Get list of users
    When I send a GET request to "/users?page=2"
    Then the response status code should be 200
    And the count of "data" child properties should be 5
    And the count of "support" properties should be 2
    And the count of "_meta" properties should be 7


  Scenario: GET and Verify data types for a list of users
    When I send a GET request to "/users?page=2"
    Then the datatypes are correct for a list of users


  Scenario Outline: GET the list of users details
    When I send a GET request to "<api>"
    Then every item in list of users response should have the expected "<parent_key>" keys: <keys>
    And every item in the list of users should have the expected "<parent_key>" keys and schema <schema>
    And the count of "<parent_key>" child properties should be <count>


  Examples:
    | api           | parent_key | keys                                                                                | schema  | count |
    | /users?page=2 | data       | id, email, first_name, last_name, avatar                                            | Data    | 5     |
    | /users?page=2 | support    | url, text                                                                           | Support | 2     |
    | /users?page=2 | _meta      | powered_by, upgrade_url, docs_url, template_gallery, message, features, upgrade_cta | Meta    | 7     |




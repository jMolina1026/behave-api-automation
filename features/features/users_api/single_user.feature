@Users @SingleUser
Feature: Single User API
  # Makes requests for the single user api

  Scenario: Get a single User
    When I send a GET request to "/users/2"
    Then the response status code should be 200


  Scenario: GET and Verify data types for a single user
    When I send a GET request to "/users/2"
    Then the data types are correct for a single user


    Scenario Outline: GET the list of users details
    When I send a GET request to "<api>"
    Then every item in the single user response should have the expected "<parent_key>" keys: <keys>
    And every item in the single user response should have the expected "<parent_key>" keys and schema <schema>
    And the count of "<parent_key>" child properties for the single user response should be <count>


  Examples:
    | api     | parent_key | keys                                                                                | schema  | count |
    | /users/1 | data       | id, email, first_name, last_name, avatar                                            | Data    | 5     |
    | /users/2 | support    | url, text                                                                           | Support | 2     |
    | /users/3 | _meta      | powered_by, upgrade_url, docs_url, template_gallery, message, features, upgrade_cta | Meta    | 7     |

#  Scenario: Not a single User is returned
##    Given the API base URL is "https://reqres.in/api"
#    When I send a GET request to "/users/23"
#    Then the response status code should be 404


#  @Post
#  Scenario: Create a new user
#    Given the API base URL is "https://reqres.in/api"
#    When I send a POST request to "/users" with body
#      """
#          {
#            "name": "Joe",
#            "job": "Dirt"
#          }
#      """
#    Then the response status code should be 201

Feature: The promotion service back-end
    As a Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my promotions

Background:
    Given the following promotions
        | name       | description          | promo_code        | start_date                | end_date             | is_active |
        | deal       | buy one get one free | b1g1free          | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | true      |
        | sale       | discount price       | offprice          | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | true      |
        | free       | free item            | free              | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | true      |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Promotion RESTful Service" in the title
    And I should not see "404 Not Found"

Scenario: Create a Promotion

Scenario: Read a Promotion

Scenario: Update a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "deal"
    And I press the "Search" button
    Then I should see "deal" in the "Name" field
    And I should see "buy one get one free" in the "description" field
    When I change "Name" to "flash sale"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "flash sale" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see "flash sale" in the results
    Then I should not see "deal" in the results
    
Scenario: Delete a Promotion

Scenario: List all Promotions

Scenario: Query a Promotion

Scenario: Cancel a Promotion

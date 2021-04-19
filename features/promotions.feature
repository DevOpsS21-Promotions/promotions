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
 When I visit the "Home Page"
 And I set the "Name" to "Promo 1"
 And I set the "Description" to "buy one get one"
 And I set the "Promo Code" to "BOGO"
 And I set the "Start Date" to "2021-06-14 12:00:00"
 And I set the "End Date" to "2021-07-13 12:00:00"
 And I select "True" in the "Active" dropdown
 And I press the "Create" button
 Then I should see the message "Success"
 When I copy the "Id" field
 And I press the "Clear" button
 Then the "Id" field should be empty
 And the "Name" field should be empty
 And the "Description" field should be empty
 And the "Start Date" field should be empty 
 And the "End Date" field should be empty
 When I paste the "Id" field
 And I press the "Retrieve" button
 Then I should see "Promo 1" in the "Name" field
 And I set the "Description" to "buy one get one"
 And I should see "BOGO" in the "Promo Code" field
 And I should see "2021-06-14 12:00:00" in the "Start Date" field 
 And I should see "2021-07-13 12:00:00" in the "End Date" field
 And I should see "True" in the "Active" dropdown

Scenario: Read a Promotion

Scenario: Update a Promotion

Scenario: Delete a Promotion

Scenario: List all Promotions

Scenario: Query a Promotion

Scenario: Cancel a Promotion

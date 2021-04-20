Feature: The promotion service back-end
    As a Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my promotions

Background:
    Given the following promotions
        | name       | description          | promo_code        | start_date                | end_date             | is_active |
        | deal       | buy one get one free | b1g1free          | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | True      |
        | sale       | discount price       | offprice          | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | True      |
        | free       | free item            | free              | 2021-04-01 12:00:00       | 2021-05-01 12:00:00  | True      |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Promotion RESTful Service" in the title
    And I should not see "404 Not Found"

Scenario: Create a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "Promo 1"
    And I set the "Description" to "Buy one get one"
    And I set the "Promo_Code" to "BOGO"
    And I set the "Start_Date" to "2021-06-14 12:00:00"
    And I set the "End_Date" to "2021-07-13 12:00:00"
    And I select "True" in the "Active" dropdown
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Description" field should be empty
    And the "Promo_code" field should be empty
    And the "Start_Date" field should be empty 
    And the "End_Date" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Promo 1" in the "Name" field
    And I should see "Buy one get one" in the "Description" field
    And I should see "BOGO" in the "Promo_Code" field
    And I should see "2021-06-14 12:00:00" in the "Start_Date" field 
    And I should see "2021-07-13 12:00:00" in the "End_Date" field
    And I should see "True" in the "Active" dropdown
    
Scenario: Read a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "Promo 2"
    And I set the "Description" to "Buy one get one two"
    And I set the "Promo_Code" to "BOGO2"
    And I set the "Start_Date" to "2021-06-14 12:00:00"
    And I set the "End_Date" to "2021-07-13 12:00:00"
    And I select "True" in the "Active" dropdown
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Description" field should be empty
    And the "Promo_code" field should be empty
    And the "Start_Date" field should be empty 
    And the "End_Date" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Promo 2" in the "Name" field
    And I should see "Buy one get one two" in the "Description" field
    And I should see "BOGO2" in the "Promo_Code" field
    And I should see "2021-06-14 12:00:00" in the "Start_Date" field 
    And I should see "2021-07-13 12:00:00" in the "End_Date" field
    And I should see "True" in the "Active" dropdown
    
Scenario: Update a Promotion

Scenario: Delete a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "Sale"
    And I press the "Search" button
    Then I should see "Sale" in the "Name" field
    Then I should see "Discount Price" in the "Description" field
    Then I should see "Offprice" in the "Promo_Code" field
    Then I should see "2021-04-01 12:00:00" in the "Start_Date" field
    Then I should see "2021-05-01 12:00:00" in the "End_Date" field
    Then I should see "True" in the "Active" dropdown
    When I press "Delete"
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Description" field should be empty
    And the "Promo_Code" field should be empty
    And the "Start_Date" field should be empty 
    And the "End_Date" field should be empty

Scenario: List all Promotions
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see "deal" in the results
    And I should see "sale" in the results
    And I should see "free" in the results
    And I should not see "percentoff" in the results

Scenario: Query a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "deal"
    And I press the "Search" button
    Then I should see "buy one get one free" in the "Description" field
    And I should see "b1g1free" in the "Promo_code" field
    And I should see "2021-04-01 12:00:00" in the "Start_date" field
    And I should see "2021-05-01 12:00:00" in the "End_date" field
    And I should see "True" in the "Active" dropdown

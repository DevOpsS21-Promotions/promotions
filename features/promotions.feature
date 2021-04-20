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

Scenario: Create a Promoption

Scenario: Read a Promoption

Scenario: Update a Promoption

Scenario: Cancel a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "Sale"
    And I press the "Search" button
    Then I should see "Sale" in the "Name" field
    Then I should see "Discount Price" in the "Description" field
    Then I should see "Offprice" in the "Promo Code" field
    Then I should see "2021-04-01 12:00:00" in the "Start Date" field
    Then I should see "2021-05-01 12:00:00" in the "End Date" field
    Then I should see "True" in the "Active" dropdown
    When I press "Cancel"
    Then I should see the message "Promotion has been Canceled"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Sale" in the "Name" field
    Then I should see "False" in the "Active" field

Scenario: Delete a Promotion

    When I visit the "Home Page"
    And I set the "Name" to "Bad Sale"
    And I set the "Description" to "bad sale"
    And I set the "Promo_Code" to "badsale"
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
    When I press "Delete"
    Then I should see the message "Promotion has been Deleted!"
    
Scenario: List all Promotions

Scenario: Query a Promoption


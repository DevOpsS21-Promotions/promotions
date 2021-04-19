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
    When I visit the "Home Page"
    And I set the "Name" to "Deal"
    And I press the "Search" button 
    Then I  should see "deal" in the "Name" field 
    And I should see "buy one get one free" in the "Description" field 
    And I should see "b1g1free" in the "Promo Code" field 
    And I should see "2021-04-01 12:00:00" in the "Start Date" field 
    And I should see "2021-05-01 12:00:00" in the "End Date" field 
    And I should see "true" in the "Active" dropdown
    
Scenario: Update a Promotion

Scenario: Delete a Promotion

Scenario: List all Promotions

Scenario: Query a Promoption

Scenario: Cancel a Promotion

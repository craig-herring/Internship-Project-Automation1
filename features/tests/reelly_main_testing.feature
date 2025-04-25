# Created by craig.herring at 4/25/25
Feature: Market Page Pagination

  Scenario: User can open market tab and go through the pagination
    Given Open the main page
    When Enter username
    And Type password
    And Log in to the page
    When Click on 'market' on the left side menu
    Then Verify the right page opens
    And Go to final page using pagination
    And Go to first page using pagination
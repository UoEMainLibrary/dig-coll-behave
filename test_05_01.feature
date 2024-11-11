Feature: I want my searches to be case-insensitive

  Scenario:
    Given I have an Archipelago environment
    When I search with terms in the main bar
    Then I get expected results
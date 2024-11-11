Feature: I want to be able to search with specific keywords and bring back content from different backends

  Scenario: running generic load succeeds
    Given I have an Archipelago environment
    When I search with terms in the main bar
    Then I get expected results
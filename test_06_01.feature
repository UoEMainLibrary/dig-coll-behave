Feature: I want boolean searches to be executable (based on "AND" or "OR")

  Scenario:
    Given I have an Archipelago environment
    When I search with terms in the main bar
    Then I get expected results
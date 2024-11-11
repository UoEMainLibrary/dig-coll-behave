Feature: I want to search on a non-Latin script
  Scenario:
	Given I have an Archipelago environment
	When I search with terms in the main bar
	Then I get expected results
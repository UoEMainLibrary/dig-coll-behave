Feature: I want advanced search to respect the field name specified
  Scenario:
	Given I have an Archipelago environment
	When I search with terms and canned fields in the advanced search area 
	Then I get expected results
Feature: I want to set up a new role with bespoke permissions
  Scenario:
	Given I have an Archipelago environment
	When I create a new role
	Then I see a user with expected permissions
Feature: I want to see my backend-sourced metadata to appear as it does in the catalogue (ie special characters correctly escaped etc)
  Scenario:
	Given I have an environment
	When I load a [see list] object from its backend
	Then I see it in Archipelago
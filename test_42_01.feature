Feature: I want to see all of my agreed metadata come through onto a loaded backend item
  Scenario:
	Given I have an environment
	When I load a [see list] object from its backend
	Then I see it in Archipelago
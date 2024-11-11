Feature: I want the system to have the capacity to store content for all of my tests
  Scenario:
	Given I have an Archipelago environment
	When I load a [see list] object from its backend
	Then The system does not fail due to lack of space
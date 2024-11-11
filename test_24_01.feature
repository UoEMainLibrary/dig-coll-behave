Feature: I want to be able to configure/administer the system as an admin
  Scenario:
	Given I have an Archipelago environment
	When I login inas Admin
	Then I see the drupal config modules
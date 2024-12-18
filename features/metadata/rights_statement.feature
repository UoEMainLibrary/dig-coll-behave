Feature: I want to see rights information on the media (page level item) that I have loaded
  Scenario: Rights information is visible on load of Goobi object
    Given I have a connection to the loading system
    And I have a connection to Archipelago
	When I load a Goobi object through media ingest (rights)
	Then I see the Goobi object with rights information in Archipelago

  Scenario: Rights information is visible on load of CSV object
    Given I have a connection to the loading system
    And I have a connection to Archipelago
	When I load a CSV object through media ingest (rights)
	Then I see the CSV object with rights information in Archipelago
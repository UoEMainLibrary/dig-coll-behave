Feature: I want to see licence information on the media (page level item) that I have loaded
  Scenario: Licence information is visible on load of Goobi object
    Given I have a connection to the loading system
    And I have a connection to Archipelago
	When I load a Goobi object through media ingest (licence)
	Then I see the Goobi object with licence information in Archipelago

  Scenario: Licence information is visible on load of CSV object
    Given I have a connection to the loading system
    And I have a connection to Archipelago
	When I load a CSV object through media ingest (licence)
	Then I see the CSV object with licence information in Archipelago
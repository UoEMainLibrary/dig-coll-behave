Feature: I want to see a book appear unpaged if it is photographed as spreads
  Scenario:
	Given I have an Archipelago environment
	When I load a [see list] object through media ingest
	Then I see it in Archipelago
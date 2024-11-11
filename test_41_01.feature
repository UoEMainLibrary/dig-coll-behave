Feature: I want to see a book appear paged if it should be paged
  Scenario:
	Given I have an Archipelago environment
	When I load a [see list] object through media ingest
	Then I see it in Archipelago
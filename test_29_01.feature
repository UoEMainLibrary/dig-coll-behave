Feature: I want to ensure checksums are recorded for a media item
  Scenario:
	Given I have an environment
	When I load a [see list] object through media ingest
	Then I see it in Archipelago
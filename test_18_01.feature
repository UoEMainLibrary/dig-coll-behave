Feature: I want to see evidence of the storage of a media file in the system in the MinIO interface
  Scenario:
	Given I have an Archipelago environment
	When I load a [see list] object through media ingest
	Then I see it in MinIO
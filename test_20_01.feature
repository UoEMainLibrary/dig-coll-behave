Feature: I want to be able to access an individual image through the IIIF image API
  Scenario:
	Given I have an Archipelago environment
	When I put an image reference into the IIIF format
	Then I see it returned appropriately
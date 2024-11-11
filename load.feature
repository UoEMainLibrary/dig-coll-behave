Feature: load content into Archipelago

  Scenario: run a generic load
     Given the system is fully initialised with the relevant backends
      And we have all the necessary media
      When we execute the media ingest process
      Then the item will appear in Archipelago
Feature: I want to load a catalogue record and its associated media

  Scenario: running generic load succeeds
    Given I have an environment
    When I load a [see list] object through media ingest
    Then I see it in Archipelago
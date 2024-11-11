Feature: I want to load media to a catalogue record that I know already exists in the system

  Scenario: running generic load succeeds
    Given I have an environment
    When I load a [see list] object through media ingest
    Then I see it in Archipelago
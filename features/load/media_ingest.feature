Feature: I want to load a catalogue record and its associated media

  Scenario: running generic load succeeds
    Given I have a connection to the loading system
    And I have a connection to Archipelago
    When I load a Goobi object through media ingest
    Then the Goobi media reaches Archipelago

  Scenario: running generic load fails if there is no connection to the system
    Given I do not have a connection to the loading system
    And I have a connection to Archipelago
    When I load a Goobi object through media ingest
    Then the Goobi media does not reach Archipelago

  Scenario: running generic load fails if there is no connection to Archipelago
    Given I have a connection to the loading system
    And I do not have a connection to Archipelago
    When I load a Goobi object through media ingest
    Then the Goobi media does not reach Archipelago

  Scenario: running generic load succeeds for CSV
    Given I have a connection to the loading system
    And I have a connection to Archipelago
    When I load a CSV object through media ingest
    Then the CSV media reaches Archipelago

  Scenario: running generic load for CSV fails if there is no connection to the system
    Given I do not have a connection to the loading system
    And I have a connection to Archipelago
    When I load a CSV object through media ingest
    Then the CSV media does not reach Archipelago

  Scenario: running generic load for CSV fails if there is no connection to Archipelago
    Given I have a connection to the loading system
    And I do not have a connection to Archipelago
    When I load a CSV object through media ingest
    Then the CSV media does not reach Archipelago

  Scenario: running generic load succeeds where catalogue record already exists
    Given I have a connection to the loading system
    And I have a connection to Archipelago
    When I load a Goobi object through media ingest
    Then the Goobi media reaches Archipelago even though the record already exists
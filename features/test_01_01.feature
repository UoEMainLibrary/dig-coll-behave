Feature: I want to load a catalogue record and make available for viewing

  Scenario: running generic load succeeds
    Given I have a connection to the loading system
    And I have a connection to Archipelago
    When I load an Alma object from its backend
    Then it reaches Archipelago

  Scenario: running generic load fails
    Given I do not have a connection to the loading system
    And I have a connection to Archipelago
    When I load an Alma object from its backend
    Then it does not reach Archipelago

  Scenario: running generic load fails
    Given I have a connection to the loading system
    And I do not have a connection to Archipelago
    When I load an Alma object from its backend
    Then it does not reach Archipelago
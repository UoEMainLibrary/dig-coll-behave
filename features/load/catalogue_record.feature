Feature: I want to load a catalogue record and make available for viewing

  Scenario: running generic load succeeds
    Given I have a connection to the loading system
    And I have a connection to Archipelago
    When I load an Alma object from its backend
    Then it reaches Archipelago

  Scenario: running generic load fails if there is no connection to the system
    Given I do not have a connection to the loading system
    And I have a connection to Archipelago
    When I load an Alma object from its backend
    Then it does not reach Archipelago

  Scenario: running generic load fails if there is no connection to Archipelago
    Given I have a connection to the loading system
    And I do not have a connection to Archipelago
    When I load an Alma object from its backend
    Then it does not reach Archipelago

  Scenario: running generic load fails if there is no connection to either system or Archipelago
    Given I do not have a connection to the loading system
    And I do not have a connection to Archipelago
    When I load an Alma object from its backend
    Then it does not reach Archipelago
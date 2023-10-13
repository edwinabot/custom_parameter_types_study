Feature: Showing off parameter types

  Scenario: Testing with a Water Cooler
    Given we are using a Water Cooler Foo
    And the fluid temperature is 20 degrees
    When we cool 10 liters of fluid by 5 degrees
    Then the fluid should be 15 degrees

  Scenario: Testing with a Air Cooler
    Given we are using a Air Cooler Bar
    And the fluid temperature is 20 degrees
    When we cool 10 liters of fluid by 50 degrees
    Then the fluid should be -30 degrees

  Scenario: Testing with a Oil Cooler
    Given we are using a Oil Cooler Baz
    And the fluid temperature is 300 degrees
    When we cool 10 liters of fluid by 180 degrees
    Then the fluid should be 120 degrees

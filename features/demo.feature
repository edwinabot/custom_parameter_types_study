Feature: showing off parameter types

  Scenario: Testing with a Water Cooler
    Given we are using a Water Cooler Foo
    And the fluid temperature is 20 degrees
    When we cool 10 liters of fluid by 5 degrees
    Then the fluid should be 5 degrees cooler

  Scenario: Testing with a Air Cooler
    Given we are using a Air Cooler Bar
    And the fluid temperature is 20 degrees
    When we cool 10 liters of fluid by 5 degrees
    Then the fluid should be 5 degrees cooler

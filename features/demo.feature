Feature: showing off parameter types

  Scenario: run a simple test
    Given we are using a Water Cooler Foo
    And the fluid temperature is 20 degrees
    When we cool 10 liters of fluid by 5 degrees
    Then the fluid should be 5 degrees cooler

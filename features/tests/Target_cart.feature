# Created by Dona at 1/7/25
Feature: Tests for cart

  Scenario: clicks on the cart icon and verifies that “Your cart is empty” message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

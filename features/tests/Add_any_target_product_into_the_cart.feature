# Created by Dona at 1/8/25
Feature: Tests for Add to Cart

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    When Click on Add to Cart button
    Then Verify Add to Cart button from right side navigation page
    Then Verify Added to cart message shown


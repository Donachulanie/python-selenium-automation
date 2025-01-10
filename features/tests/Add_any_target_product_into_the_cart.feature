# Created by Dona at 1/8/25
Feature: Tests for Add to Cart

#  Scenario: User can add a product to cart
#    Given Open target main page
#    When Search for coffee
#    And Click on Add to Cart button
#    And Verify Add to Cart button from right side navigation page
#    Then Verify Added to cart message shown

#  Scenario: User can add a product to cart
#    Given Open target main page
#    When Search for coffee
#    And Click on Add to Cart button
#    And Verify Add to Cart button from right side navigation page
#    And Open cart page
#    Then Verify cart has 1 item(s)


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Verify Add to Cart button from right side navigation page
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
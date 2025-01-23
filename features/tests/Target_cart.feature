# Created by Dona at 1/7/25
Feature: Tests for cart functionality

  Scenario: clicks on the cart icon and verifies that “Your cart is empty” message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Verify Add to Cart button from right side navigation page
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



#    Scenario: User can add a product to cart
#    Given Open target main page
#    When Search for mug
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
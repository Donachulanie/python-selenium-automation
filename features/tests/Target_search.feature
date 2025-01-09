# Created by Dona at 1/6/25
Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a product
    Given Open target main page
    When Search for mug
    Then Verify search results shown for mug

#  Scenario Outline: User can search for a product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results shown for <product>
#    Examples:
#      | product |
#      | tea     |
#      | coffee  |
#      | mug     |



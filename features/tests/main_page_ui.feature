# Created by Dona at 1/8/25
Feature: Tests for main page ui


  Scenario: User can see header links
    Given Open target main page
    Then Verify at least 1 header link is shown

  Scenario: User can see 6 header links
    Given Open target main page
    Then Verify 6 header links are shown


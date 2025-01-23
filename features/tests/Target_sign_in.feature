# Created by Dona at 1/7/25
Feature: Tests for sign in

  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click on Sign in icon
    Then Verify "Sign in" text shown
    When Click on sign in icon in the loaded page
    Then Verify "Sign into your Target account" text is shown



  Scenario: Login test
    Given Open target main page
    When Click on Sign in icon
    Then Verify "Sign in" text shown
    When Click on sign in icon in the loaded page
    Then Verify "Sign into your Target account" text is shown
    When input valid clay25@pickuplanet.com and David1999@ on sign in page
    Then Click on the "Sign in with password" icon
    Then Verify user is logged in successfully







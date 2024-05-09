
Feature:

  @sample01
  Scenario Outline: Verify the login functionality
    Given I Launch the application url

    Examples:
      | Username | Password |
      | 123      | 123      |
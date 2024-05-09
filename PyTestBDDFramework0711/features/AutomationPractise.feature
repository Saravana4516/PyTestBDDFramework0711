Feature:

  #Sample test case for UI Validation
  @TC01_Automation
  Scenario Outline: Verify the User is able to add the products in QA environment
    Given I Launch the application url "<env>"
    Then click on shop menu item
    Then Add Selenium Ruby product to the cart
    Then Click on view basket
    Then Click on proceed to checkout button


   # Then click on home menu button


    Examples:
      | Username | Password | env |
      | 123      | 123      | QA  |


  @TC02_Automation
  Scenario Outline: Verify the User is able to Call APIs and parsing
    Given I call APIs and verify parsing



   # Then click on home menu button


    Examples:
      | Username | Password | env |
      | 123      | 123      | QA  |




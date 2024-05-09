import pytest
from pytest_bdd import scenario, then, parsers, given, when
from pages.AutomationPractise import AutomationPractise


@pytest.mark.parametrize(['Username','Password'], [('', '')])
@scenario('../features/AutomationPractise.feature', 'Verify the User is able to add the products in QA environment')
def test_TC01_Automation(Username,Password):
    """"""

@pytest.mark.parametrize(['Username','Password'], [('', '')])
@scenario('../features/AutomationPractise.feature', 'Verify the User is able to Call APIs and parsing')
def test_TC02_Automation(Username,Password):
    """"""


@then('click on shop menu item')
def step_impl(init_driver):
    # init_driver.get(GlobalVariables.url)
    AP = AutomationPractise(init_driver)
    AP.HomemenuCLick()


#Add Selenium Ruby product to the cart
@then('Add Selenium Ruby product to the cart')
def step_impl(init_driver):
    AP = AutomationPractise(init_driver)
    AP.AddSeleniumRuby()

#lick on view basketC
@then('Click on view basket')
def step_impl(init_driver):
    AP = AutomationPractise(init_driver)
    AP.ViewBasketVerify()

#Click on proceed to checkout button
@then('Click on proceed to checkout button')
def step_impl(init_driver):
    AP = AutomationPractise(init_driver)
    AP.ProceedCheckout()

#I call APIs and verify parsing
@given('I call APIs and verify parsing')
def step_impl(init_driver):
    AP = AutomationPractise(init_driver)
    AP.CallAPIs()




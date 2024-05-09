import time
from datetime import date
import sys
import os

import allure
import requests
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

sys.path.append(os.path.dirname("/Users/saravanakumar/PycharmProjects/pythonProject/Automation/utilities"))
from utilities import GlobalVariables

class AutomationPractise:

    Shopxpath = "//a[text()='Shop']"
    SeleniumRubyProduct = "//img[@alt='Selenium Ruby']/parent::a/following-sibling::a"
    Productadded = "//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart added']"
    ViewBasket = "//a[@title='View Basket']"
    ProceedToCheckout = "//a[@class='checkout-button button alt wc-forward']"

    def __init__(self,driver):
        self.driver = driver

    def HomemenuCLick(self):
        self.driver.find_element(by=By.XPATH, value = self.Shopxpath).click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="HomemenuCLick",attachment_type=AttachmentType.PNG)


    def AddSeleniumRuby(self):
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value = self.SeleniumRubyProduct).click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="addSeleniumRubyProduct",attachment_type=AttachmentType.PNG)
        try:
            self.driver.find_element(by=By.XPATH, value=self.Productadded)
            print("Product added")
        except:
            print("Product not added suucessfully,hence failed")
            assert False,"Product not added suucessfully,hence failed"


    def ViewBasketVerify(self):
        self.driver.find_element(by=By.XPATH, value = self.ViewBasket).click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="ViewBasket",attachment_type=AttachmentType.PNG)


    def ProceedCheckout(self):
        self.driver.find_element(by=By.XPATH, value = self.ProceedToCheckout).click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="ProceedToCheckout",attachment_type=AttachmentType.PNG)


    def CallAPIs(self):
        response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
        # print(response.text)
        # print(type(response.text))
        # dict_response = json.loads(response.text)
        # print(dict_response[0]['isbn'])
        json_response = response.json()
        print(json_response)
        print(type(json_response))
        print(json_response[0]['isbn'])
        assert response.status_code == 200
        print(response.headers)
        assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
        # Retrieve the book details with ISBN RGHCC
        for actualBook in json_response:
            if actualBook['isbn'] == 'RGHCC':
                print(actualBook)
                break

        expectedBook = {
                "book_name": "Learn API Automation with RestAssured",
                "isbn": "RGHCC",
                "aisle": "12239"
            }

        print(expectedBook)


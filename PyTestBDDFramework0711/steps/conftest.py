
import time

import pytest
import yaml
from pytest_bdd import scenario, then,parsers,given,when
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


import sys
import os
sys.path.append(os.path.dirname("/Users/saravanakumar/PycharmProjects/pythonProject/Automation/utilities"))
from utilities import GlobalVariables


@pytest.fixture(scope='class')
def init_driver():
    with open('config/envInfo.yaml', 'r') as f:
        info = yaml.safe_load(f)
    if info["REGION"]["QA"]["browser"] == "chrome":
        service =Service(executable_path='drivers/chromedriver')
        options=webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service,options=options)
        driver.maximize_window()
        time.sleep(2)
    else:
        driver = webdriver.Ie("Location of the IE Driver")

    yield driver
    driver.close()
    driver.quit()

@given(parsers.cfparse('I Launch the application url "{env}"'))
def launch_app(init_driver,env):
    with open('config/envInfo.yaml', 'r') as f:
        info = yaml.safe_load(f)
    if (env == 'QA'):
        GlobalVariables.url = info["REGION"]["QA"]["url"]

    init_driver.get(GlobalVariables.url)
    #init_driver.get("https://www.flipkart.com/")

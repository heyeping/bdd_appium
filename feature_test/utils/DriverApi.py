#@project:  bdd_appium
#@author: heyeping
#@file: DriverApi.py
#@ide: PyCharm
#@time: 2021/11/1 6:23 PM
from behave import *
from appium import webdriver as driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

class DriverApi:

    def find_element_until_visibility(self, by=By.ID, locator="", timeout=10):
        ele = WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(EC.visibility_of_element_located((by, locator)))
        return ele

    def find_elements_until_visibility(self, by=By.ID, locator="", timeout=10):
        eles = WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
            EC.visibility_of_any_elements_located((by, locator)))
        return eles

    # 判断元素是否存在
    def is_element(self, by=By.ID, locator="", timeout=50):
        Flag = None
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency=1).until(
                EC.visibility_of_element_located((by, locator)))
            logger.info("定位到{locator}元素存在".format(locator=locator))
            Flag = True
            return Flag
        except TimeoutException:
            Flag = False
            return Flag
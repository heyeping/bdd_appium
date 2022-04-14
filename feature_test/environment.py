#@project:  bdd_appium
#@author: heyeping
#@file: environment.py.py
#@ide: PyCharm
#@time: 2021/7/16 3:36 PM

import os
from appium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Remote(
        command_executor= 'http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "9",
            "udid": "61b32542",
            "appPackage": "com.ayla.hotelsaas",
            "appActivity": "com.ayla.hotelsaas.ui.SPlashActivity",
            "noReset": True,
            "deviceName": "xiaoxiao8",
            "autoGrantPermissions": True
        }
    )
    #隐式等待10s
    context.driver.implicitly_wait(10)

def after_feature(context, feature):
    context.driver.quit()
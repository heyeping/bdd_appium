from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from feature_test.utils.DriverApi import DriverApi
import time
use_step_matcher("re")

def find_element_until_visibility(driver, by=By.ID, locator="", timeout=10):
    ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_element_located((by, locator)))
    return ele

def find_elements_until_visibility(driver, by=By.ID, locator="", timeout=10):
    ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_any_elements_located((by, locator)))
    return ele

@given("项目名称 通过bdd脚本创建")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("在首页点击添加按钮")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #time.sleep(2)
    el = find_element_until_visibility(context.driver, by=By.ID, locator='com.ayla.hotelsaas:id/bt_add')
    el.click()


@step("输入项目名称 通过bdd脚本创建的")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    el = find_element_until_visibility(context.driver, by=By.ID, locator='ed_name')
    el.click()
    name_field = find_element_until_visibility(context.driver, by=By.ID, locator='et_dsn')
    name_field.clear()
    name_field.set_value('通过bdd脚本创建')
    v_done = find_element_until_visibility(context.driver, by=By.ID, locator='v_done')
    v_done.click()


@step("点击 保存 按钮")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    el = find_element_until_visibility(context.driver, by=By.ID, locator='tv_right')
    el.click()


@then("验证列表中最新的项目名称")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    els = find_elements_until_visibility(context.driver, by=By.ID, locator='tv_title')
    name = els[1].text
    assert name == '通过bdd脚本创建'
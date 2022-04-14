"""YW-1257 feature tests."""
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
rootPath2 = os.path.split(rootPath1)[0]
rootPath3 = os.path.split(rootPath2)[0]
print(curPath)
#rf路径声明
sys.path.append(curPath)
from pytest_bdd import given,scenario,then,when



@scenario('yw-1257.feature', 'test_report')
def test_report():
    """test_report"""


@given('test bp report')
def bp_report():
    """test bp report"""
    pass


@when('pull report')
def cpull_report():
    """pull report"""
    pass


@then('report success')
def report_success():
    """report success"""
    pass


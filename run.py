#@project:  bdd_appium
#@author: heyeping
#@file: run.py.py
#@ide: PyCharm
#@time: 2021/7/20 11:10 AM

import glob
from behave.__main__ import main as behave_main
import datetime
import os
import shutil

if __name__ == '__main__':
    #设置执行命令和保存路径
    code_path = os.path.dirname(os.path.realpath(__file__))
    #改变当前工作目录到知道路径
    os.chdir(code_path)
    result_folder = "report/" + datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    #print(result_folder)
    run_cmd = ["-f allure_behave.formatter:AllureFormatter", "-o" + "allure-results"]

    #定位feature文件
    ff = glob.glob(code_path + '/feature_test/{feature_name}.feature'.format(feature_name="hotel_app"))
    run_cmd.extend(ff)

    #通过Behave源码执行脚本并将结果保存为json文件到allure-results目录下
    behave_main(run_cmd)

    #将json结果转换为html
    os.system("allure generate --report-dir {folder}/html/ {result} ".format(folder=code_path + "/" + result_folder, result="allure-results"))

    #递归删除生成结果目录
    shutil.rmtree("allure-results")

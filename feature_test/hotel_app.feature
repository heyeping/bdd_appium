# Created by heyeping at 2021/7/15
Feature: 创建项目
#Enter feature name here
  # Enter feature description here

  Scenario: 正常创建酒店项目
    Given 项目名称 通过bdd脚本创建
    When 在首页点击添加按钮
    And 输入项目名称 通过bdd脚本创建的
    And 点击 保存 按钮
    Then 验证列表中最新的项目名称
  # Enter scenario name here
    # Enter steps here


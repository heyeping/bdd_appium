Feature: YW-1257

  @YW-1257 @OPEN
  Scenario: test_report
    Given test bp report
    When pull report
    Then report success

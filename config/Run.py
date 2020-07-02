import HTMLTestRunner
import unittest
import os


# 添加测试用例至suite中
def creatsuite():
    suite = unittest.TestSuite()
    test_path = os.path.dirname(os.path.abspath(".")) + os.sep + "testcase"
    discover = unittest.defaultTestLoader.discover(test_path, pattern="*.py")
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTests(test_case)
    return suite

if __name__ == '__main__':
    report_path = os.path.dirname(os.path.abspath(".")) + os.sep + "Report" + os.sep + "report.html"  # 测试报告地址
    stream = open(report_path, "w", encoding="utf-8")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="测试报告", description="测试报告详情")
    runner.run(creatsuite())


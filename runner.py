import os
import unittest
import HtmlTestRunner

suite = unittest.defaultTestLoader.discover('testCase', 'test_unittest.py')
runner = HtmlTestRunner.HTMLTestRunner(report_title='试用测试报告')
runner.run(suite)


# report_dir = 'C:\\Users\\chenminhua\\PycharmProjects\\Vip6UIappium\\report'
# report_html = os.path.join(report_dir, 'report.html')
# print(report_html)
# with open(report_html, 'w') as f:
#     runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_title='试行测试报告')
#     runner.run(suite)
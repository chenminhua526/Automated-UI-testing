import time
import unittest
import HtmlTestRunner
from common.sendEmail import EmailSending
from common.handleReport import get_new_report


# 1、加载用例
suite = unittest.defaultTestLoader.discover('testCase', 'test_ui.py')
# 2、实例化runner，执行用例并生成报告
runner = HtmlTestRunner.HTMLTestRunner(report_title='试用测试报告')
runner.run(suite)
time.sleep(3)
# 3、获取最新的报告
new_report = get_new_report()
# 4、发送邮件
Email = EmailSending(new_report)
Email.send()




# 另一版本HTMLTestRunner用法
# report_html = os.path.join(report_dir, 'report.html')
# print(report_html)
# with open(report_html, 'w') as f:
#     runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_title='试行测试报告')
#     runner.run(suite)

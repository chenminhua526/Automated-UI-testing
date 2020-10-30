import os
import re
import time
import unittest
import HtmlTestRunner
from common.configEmail import EmailSending

suite = unittest.defaultTestLoader.discover('testCase', 'test_*.py')
runner = HtmlTestRunner.HTMLTestRunner(report_title='试用测试报告')
runner.run(suite)
time.sleep(3)
# 获取最新的报告
base_path = os.getcwd()
reports_dir = os.path.join(base_path, 'reports')
# 获取所有报告名称
report_files = os.listdir(reports_dir)
# 将报告文件名中的时间取出
p = re.compile(r'MyTest_(?P<year>.+)-(?P<month>.+)-(?P<data>.+)_(?P<hour>.+)-(?P<minute>.+)-(?P<second>.+).html')
time_list = []
for i in report_files:
    groups = p.search(i).groups()
    create_time = ''
    for j in groups:
        create_time += j
    create_time = int(create_time)
    time_list.append(create_time)
# 得到最近的时间
new_time = max(time_list)
index = time_list.index(new_time)
# 得到最近的报告
new_report = report_files[index]
report_path = os.path.join(reports_dir, new_report)
# 发送邮件
Email = EmailSending(report_path)
Email.send()

# report_dir = 'C:\\Users\\chenminhua\\PycharmProjects\\Vip6UIappium\\report'
# report_html = os.path.join(report_dir, 'report.html')
# print(report_html)
# with open(report_html, 'w') as f:
#     runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_title='试行测试报告')
#     runner.run(suite)
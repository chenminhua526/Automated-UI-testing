import html
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig import ReadConfig


configs = ReadConfig()


class EmailSending(object):

    def __init__(self, report_file):
        self.smtp_server = configs.get_Email_conf('smtpServer')
        self.sender = configs.get_Email_conf('EmailSender')
        self.auth_code = configs.get_Email_conf('authCode')
        self.recipients = configs.get_Email_conf('recipients')
        self.report = report_file

    def set_message(self):
        """邮件内容"""
        # 邮件主题
        subject = "UI自动化测试报告"
        # 获取报告内容
        with open(self.report, 'rb') as f:
            content = f.read().decode()
        # html-report中有单引号转义符
        body = html.unescape(content)
        # 设置邮件信息
        message = MIMEMultipart()
        message['subject'] = subject
        body = MIMEText(body, 'html', 'utf-8')
        message.attach(body)
        # 添加附件
        att = MIMEText(open(self.report, 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="report.html"'
        message.attach(att)
        return message

    def send(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(self.sender, self.auth_code)
        message = self.set_message()
        smtp.sendmail(self.sender, self.recipients, message.as_string())
        smtp.quit()



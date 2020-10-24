import os,time
from appium import webdriver


class Driver:

    def __init__(self):
        self.command_executor = 'http://127.0.0.1:4723/wd/hub'
        self.desire_caps = {
            "deviceName": "192.168.31.137:5555",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True
        }
        self.driver = None

    def start_up(self):
        print("启动中……")
        # 启动app
        self.driver = webdriver.Remote(self.command_executor, self.desire_caps)
        print("启动完成")
        return self.driver

    def quit(self):
        self.driver.quit()








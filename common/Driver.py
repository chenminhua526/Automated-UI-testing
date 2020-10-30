import os,time
from appium import webdriver
from common.readConfig import ReadConfig


class Driver:

    def __init__(self):
        configs = ReadConfig()
        server_ip = configs.get_server_conf('ip')
        server_port = configs.get_server_conf('port')
        self.command_executor = 'http://{}:{}/wd/hub'.format(server_ip, server_port)

        # 设置启动参数
        """
        {
            "deviceName": "192.168.31.137:5555",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": true,
            "unicodeKeyboard": true
        }
        """
        device_name = configs.get_device_conf('deviceName')
        platform_name = configs.get_device_conf('platform')
        platform_version = configs.get_device_conf('version')
        app_package = configs.get_app_conf('appPackage')
        app_activity = configs.get_app_conf('appActivity')
        self.desire_caps = {
            "deviceName": device_name,
            "platformName": platform_name,
            "platformVersion": platform_version,
            "appPackage": app_package,
            "appActivity": app_activity,
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







import configparser
import os


class ReadConfig:

    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file = path + '\\config.ini'
        # self.config_file = "C:\\Users\\chenminhua\\PycharmProjects\\Vip6UIappium\\config.ini"
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_file, encoding='utf-8')

    # def get_sections(self):
    #     sections = self.conf.sections()
    #     # print(sections)
    #     return sections
    #
    # def get_options(self, section):
    #     options = self.conf.options(section)
    #     # print(options)
    #     return options
    #
    # def get_items(self, section):
    #     items = self.conf.items(section)
    #     # print(items)
    #     return items

    def get_value(self, section, option):
        try:
            value = self.conf.get(section, option)
            # print(value)
            return value
        except Exception as e:
            print("无法识别的section或option，提示：", e)

    def get_server_conf(self, option):
        section = "server"
        return self.get_value(section, option)

    def get_device_conf(self, option):
        section = "device"
        return self.get_value(section, option)

    def get_app_conf(self, option):
        section = "app"
        return self.get_value(section, option)

    def get_Email_conf(self, option):
        section = "Email"
        value = self.get_value(section, option)
        # print(value)
        if option == 'recipients':
            value_list = value.split(',')
            return value_list
        else:
            return value








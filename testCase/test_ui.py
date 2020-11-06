import time
import unittest

from common.MyTest import MyTest
from common.readData import ReadExcel
from PO.HomePage import HomePage
from PO.PublishHeadlinePage import PublishHeadlinePage

test_data = ReadExcel('data.xlsx', 'Sheet1')


class TestPublishShortNews(MyTest):

    # 发布微头条
    def test_publish_headline_normal(self):
        home_page = HomePage(self.driver)
        home_page.click_publish()  # 点击发布按钮
        home_page.click_edit_headline()  # 选择微头条
        # 获取测试数据--微头条内容
        # class_name = self.__class__.__name__
        # method_name = self._testMethodName
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        publish_headline_page = PublishHeadlinePage(self.driver)
        publish_headline_page.send_keys_content(value)  # 输入微头条内容
        publish_headline_page.click_publish()  # 点击发布
        time.sleep(3)

    @unittest.skip('跳过')
    def test_publish_headline_min_len(self):
        # 发布微头条--最小长度
        home_page = HomePage(self.driver)
        home_page.click_publish()  # 点击发布按钮
        home_page.click_edit_headline()  # 选择微头条
        # 获取测试数据--微头条内容
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        publish_headline_page = PublishHeadlinePage(self.driver)
        publish_headline_page.send_keys_content(value)  # 输入微头条内容
        publish_headline_page.click_publish()  # 点击发布
        time.sleep(3)

    @unittest.skip('跳过')
    def test_publish_headline_max_len(self):
        # 发布微头条--最大长度
        home_page = HomePage(self.driver)
        home_page.click_publish()  # 点击发布按钮
        home_page.click_edit_headline()  # 选择微头条
        # 获取测试数据--微头条内容
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        publish_headline_page = PublishHeadlinePage(self.driver)
        publish_headline_page.send_keys_content(value)  # 输入微头条内容
        publish_headline_page.click_publish()  # 点击发布
        time.sleep(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)


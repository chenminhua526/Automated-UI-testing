import time
import unittest

from common.MyTest import MyTest
from common.readData import ReadExcel

test_data = ReadExcel('data.xlsx', 'Sheet1')


class TestPublishShortNews(MyTest):

    def test_publish_short_news_normal(self):
        # 发布微头条
        self.driver.find_element_by_id("com.ss.android.article.news:id/cfw").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        # class_name = self.__class__.__name__
        # method_name = self._testMethodName
        # print('类名：', class_name)
        # print('方法名：', method_name)
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        self.driver.find_element_by_id("com.ss.android.article.news:id/adp").send_keys(value)
        time.sleep(1)
        self.driver.find_element_by_id("com.ss.android.article.news:id/d_1").click()
        time.sleep(1)

    @unittest.skip('跳过')
    def test_publish_short_news_min_len(self):
        # 发布微头条--最小长度
        self.driver.find_element_by_id("com.ss.android.article.news:id/cfw").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        self.driver.find_element_by_id("com.ss.android.article.news:id/adp").send_keys(value)
        time.sleep(1)
        self.driver.find_element_by_id("com.ss.android.article.news:id/d_1").click()
        time.sleep(1)

    @unittest.skip('跳过')
    def test_publish_short_news_max_len(self):
        # 发布微头条--最大长度
        self.driver.find_element_by_id("com.ss.android.article.news:id/cfw").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        value = test_data.get_case_data(self.__class__.__name__, self._testMethodName)
        self.driver.find_element_by_id("com.ss.android.article.news:id/adp").send_keys(value)
        time.sleep(1)
        self.driver.find_element_by_id("com.ss.android.article.news:id/d_1").click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main(verbosity=2)


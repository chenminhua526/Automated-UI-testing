import time
import unittest

from common.Driver import Driver


class TestOne(unittest.TestCase):
    driver = Driver()

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.driver.start_up()
        time.sleep(3)

    def test_publish_short_news(self):
        # 发布微头条
        self.driver.find_element_by_id("com.ss.android.article.news:id/cfw").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.ss.android.article.news:id/adp").send_keys("微头条2")
        time.sleep(1)
        self.driver.find_element_by_id("com.ss.android.article.news:id/d_1").click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)


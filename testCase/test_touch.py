"""
练习触屏操作：
1、driver.tap()
2、TouchAction类
3、driver.swipe()
"""
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction
from common.Public import Swipe
from common.MyTest import MyTest


class TestPublishShortNews(MyTest):

    @unittest.skip('skip')
    def test_tap(self):
        self.driver.tap([(48, 383), (673, 442)], 500)  # 点击推荐置顶文章
        time.sleep(2)
        self.driver.back()
        time.sleep(1)

    @unittest.skip('skip')
    def test_touchAction(self):
        self.driver.tap([(909, 2220), (981, 2259)], 500)
        self.driver.find_element_by_id('com.ss.android.article.news:id/b9t').click()
        time.sleep(1)
        action = TouchAction(self.driver)
        # 将设置页面提示音开关活动关闭
        action.press(x=979, y=1567).move_to(x=892, y=1567).release().perform()
        time.sleep(2)
        # TouchAction还有tap() ,longPress()等方法

    def test_swipe(self):
        # 测试上下左右滑动操作
        swipe = Swipe(self.driver)
        swipe.swipe_up()
        time.sleep(1)
        swipe.swipe_down()
        time.sleep(1)
        swipe.swipe_left()
        time.sleep(2)
        swipe.swipe_right()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

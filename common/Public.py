"""
封装上下左右滑动屏幕操作
"""


class Swipe:

    def __init__(self, driver):
        self.driver = driver

    def get_size(self):
        # size = self.driver.get_window_size()
        # print(size)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向上滑动屏幕
    def swipe_up(self):
        size = self.get_size()
        x = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75) # 起始y坐标
        y2 = int(size[1] * 0.25) # 结束y坐标
        self.driver.swipe(x, y1, x, y2, duration=0)

    # 向下滑动屏幕
    def swipe_down(self):
        size = self.get_size()
        x = int(size[0] * 0.5)
        y1 = int(size[1] * 0.25)  # 起始y坐标
        y2 = int(size[1] * 0.75)  # 结束y坐标
        self.driver.swipe(x, y1, x, y2, duration=0)

    # 向左滑动屏幕
    def swipe_left(self):
        size = self.get_size()
        x1 = int(size[0] * 0.75)  # 起始x坐标
        x2 = int(size[0] * 0.25)  # 结束x坐标
        y = int(size[1] * 0.5)
        self.driver.swipe(x1, y, x2, y, duration=0)

    # 向右滑动屏幕
    def swipe_right(self):
        size = self.get_size()
        x1 = int(size[0] * 0.25)  # 起始x坐标
        x2 = int(size[0] * 0.75)  # 结束x坐标
        y = int(size[1] * 0.5)
        self.driver.swipe(x1, y, x2, y, duration=0)



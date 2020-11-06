from selenium.webdriver.common.by import By
from PO.BasePage import BasePage


class PublishHeadlinePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # 微头条内容编辑框的定位方式
        self.content = (By.ID, "com.ss.android.article.news:id/adu")
        # 发布按钮的定位元素
        self.publish = (By.ID, "com.ss.android.article.news:id/db9")

    # 输入微头条内容
    def send_keys_content(self, value):
        self.until_find_element(*self.content).send_keys(value)

    # 点击发布按钮
    def click_publish(self):
        self.until_find_element(*self.publish).click()

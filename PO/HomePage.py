"""
主页
"""
from selenium.webdriver.common.by import By
from PO.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # 发布按钮的定位方式
        self.publish = (By.ID, "com.ss.android.article.news:id/cht")
        # 点击编辑微头条的定位元素
        self.headline = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")

    # 点击发布按钮
    def click_publish(self):
        self.until_find_element(*self.publish).click()

    # 点击编辑微头条
    def click_edit_headline(self):
        self.until_find_element(*self.headline).click()



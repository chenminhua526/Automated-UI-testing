from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def until_find_element(self, *items):
        # WebDriverWait类用于实现显示等待
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(items))

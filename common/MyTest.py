import time
import unittest
from common.Driver import Driver


class MyTest(unittest.TestCase):
    driver = Driver()

    @classmethod
    def setUpClass(cls):
        print('执行setUpClass……')
        cls.driver = cls.driver.start_up()
        # cls.driver = Driver().start_up()

    def setUp(self):
        print('执行setUp……')
        self.driver.launch_app()
        time.sleep(8)

    def tearDown(self):
        print('执行tearDown……')
        self.driver.close_app()

    @classmethod
    def tearDownClass(cls):
        print('执行tearDownClass……')
        cls.driver.quit()

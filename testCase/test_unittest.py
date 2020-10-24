"""
unittest练习用
"""
from ddt import ddt, data, unpack
import unittest

test_data = [1, 2, 3]


@ddt  # 代表这个测试类使用ddt数据驱动
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('测试前环境准备')

    @classmethod
    def tearDownClass(cls):
        print('测试后环境还原')

    def setUp(self):
        print('用例执行准备')

    def tearDown(self):
        print('用例执行后处理')

    @data(*test_data)
    def test_one(self, data):
        print(data)

    @data(*((1, 2), (1, 'a'), (2, 2)))
    @unpack
    def test_two(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1, value2)


if __name__ == "__main__":
    unittest.main(verbosity=2)


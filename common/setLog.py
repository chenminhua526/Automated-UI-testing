import logging
import os
import time


class Logger(object):

    def __init__(self):
        """定义logger的基本设置"""
        # 指定日志输出格式
        self._formatter = logging.Formatter('%(asctime)s-'
                                  '%(levelname)s-'
                                  '%(filename)s-'
                                  '%(threadName)s-'
                                  '[line:%(lineno)d]-'
                                  '%(name)s-'
                                  '日志信息：%(message)s')

        # 指定日志输出目录
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._log_dir = os.path.join(path, "logs")

        # 创建日志实例，日志名称用来唯一确定同一个日志对象
        self._logger = logging.getLogger('automation_log')
        self._logger.setLevel(logging.INFO)

        # 判断是否已经有实例对象，如果没有的话再添加句柄，防止日志重复打印
        if not self._logger.handlers:
            # 添加日志句柄
            self._logger.addHandler(self._get_console_handler())
            self._logger.addHandler(self._get_file_handler())

    def _get_console_handler(self):
        """设置控制台输出的句柄"""
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self._formatter)
        return ch

    def _get_file_handler(self):
        """设置文件输出的句柄"""
        time_str = time.strftime('%Y-%m-%d')
        file = self._log_dir + "\\" + "auto_test_" + time_str + "_log.txt"
        # 输出到file
        fh = logging.FileHandler(file, mode='a',
                                 encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self._formatter)
        return fh

    def get_logger(self):
        """对外提供logger实例"""
        return self._logger


# 预设实例，作为单例，给外部模块使用
logger = Logger().get_logger()

if __name__ == '__main__':
    logger.info('1111')

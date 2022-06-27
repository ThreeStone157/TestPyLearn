# coding:utf-8
import logging
import time
from logging.handlers import TimedRotatingFileHandler


# 封装的日志类
class MyLogger(object):

    @staticmethod
    def create_logger():
        my_logger = logging.getLogger()
        my_logger.setLevel("DEBUG")
        seconds = int(time.time())
        # 控制台处理器
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel("ERROR")
        my_logger.addHandler(stream_handler)
        # 使用时间滚动的文件处理器
        log_file_handler = TimedRotatingFileHandler(filename='{}.txt'.format(seconds).format(), when='D', interval=1, backupCount=10,encoding="utf8")
        log_file_handler.setLevel("INFO")
        my_logger.addHandler(log_file_handler)
        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        stream_handler.setFormatter(formatter)
        log_file_handler.setFormatter(formatter)
        return my_logger


if __name__ == "__main__":
    my_log = MyLogger()
    my_log.create_logger()
    logging.info("这个是Info等级的日志")
    logging.warning("这个是Warning等级的日志")
    logging.error("这个是error等级的日志")
    logging.critical("这个是critical等级的日志")
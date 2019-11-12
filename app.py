#封装接口前缀、
import logging
import os
import logging.handlers

BASE_URL = "http://182.92.81.159"

FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)

TOKEN = None
ID = None



def my_log_config():
    # 1. 获取日志对象
    logger = logging.getLogger()
    # 2. 为日志对象设计输出日志级别
    logger.setLevel(logging.INFO)
    # 3. 设置日志的输出目标(多目标)
    to_1 = logging.StreamHandler()  # 默认到控制台
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/hello.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=10,
                                                     encoding="utf-8")
    # 4. 指定输出格式
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 5. 组合: 输出格式与输出目标和日志对象相组合
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)

#调用日志
# my_log_config()
# logging.info("hello")
import configparser
import os

def get_option(section, option):
    path = os.path.dirname(os.path.abspath(".")) + os.sep + "config"  # 获取config路径
    conf = os.path.join(path, "config.ini")  # 找到 config.ini文件
    config = configparser.ConfigParser()
    config.read(conf)  # 读取config.ini文件
    res = config.get(section, option)
    return res


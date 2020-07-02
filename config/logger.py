import logging
import os.path
import time

class Lagger(object):

    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 定义日志的级别

        # 创建一个handler,用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        # 项目根目录下/Logs 保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/Logs/'  # 日志存放地址
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler,用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

import unittest
import pandas as pd
import os
import time
from selenium import webdriver
from config.Get_section import get_option
from config.logger import Lagger
from pageElement.login_Element import login

logger = Lagger(logger="login").get_log()  # 定义日志级别为login

class Mytest(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 隐式等待
        self.driver.maximize_window()
        path = os.path.dirname(os.path.abspath(".")) + os.sep + "pageElement" + os.sep + "data.xlsx"
        # 读取Excel中内容，df为返回的多维数组，即Excel的所有内容，dtype=object表示保留Excel原有的样子（不加会将数字转换为float型）
        self.df = pd.read_excel(path, sheet_name="login", dtype=object)

    def tearDown(self):
        self.driver.quit()

    def add_img(self):  # 在测试报告中放入截图
        self.imgs.append(self.driver.get_screenshot_as_base64())

    # 后台用户登录
    def test_01(self):
        url = get_option("url", "test_url")
        self.driver.get(url)
        logger.info("test01:Get url and visit")

        # 调用页面元素
        self.driver.find_element_by_xpath(login.login_xpath).click()
        self.driver.find_element_by_xpath(login.username_xpath).send_keys(self.df["username"][0])
        self.driver.find_element_by_xpath(login.password_xpath).send_keys(self.df["password"][0])
        # self.driver.find_element_by_xpath(login.verification_xpath).send_keys(self.df["verification"][0])
        self.driver.find_element_by_xpath(login.login_in_xpath).click()
        self.driver.find_element_by_xpath(login.login_user_xpath).click()  # 点击用户名，显示下拉窗口

        try:
            self.assertEqual(self.driver.find_element_by_xpath(login.login_out_xpath).text, "退出登录")
            logger.info("test01:登录成功")
        except AssertionError:
            self.add_img()
            self.assertTrue(False)  # 断言失败
            logger.info("test01:Test Case execute fail")

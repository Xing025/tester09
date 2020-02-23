#coding=utf-8
from selenium import webdriver
import unittest
import time

driver=webdriver.Firefox()
driver.get('http://www.testertechnology.com/forum')

#通过driver.title获取页面title并打印 是字符串类型的
title=driver.title
#下面隐藏的是自己写的，是错误的
# class Test(unittest.TestCase):
#     def test01(self):
#         self.assertEqual(driver.title,"TesterTT测试区")

print(title)
print(type(title))

#通过css_selector（）定位控件：精品贴 并点击
driver.find_element_by_css_selector("span#postCata>a:nth-child(2)").click()
time.sleep(5)

#通过driver.current_url获取当前页面url地址并打印 是字符串类型的
url=driver.current_url
print(type(url))
print(url)

driver.quit()

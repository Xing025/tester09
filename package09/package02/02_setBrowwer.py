#coding=utf-8
from selenium import webdriver
import unittest
import time

driver=webdriver.Firefox()
driver.get('http://www.testertechnology.com/forum')
#通过css_selector（）定位控件：精品贴 并点击
driver.find_element_by_css_selector("span#postCata>a:nth-child(2)").click()
time.sleep(5)
time.sleep(5)
time.sleep(2)
driver.quit()
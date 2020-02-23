#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://182.92.197.48:8080/forum')
time.sleep(3)
driver.find_element_by_id("index_search_words").send_keys("如何开发企业需求")
time.sleep(3)
driver.find_element_by_xpath("//form[@id='postsSearch']/i").click()
driver.quit()


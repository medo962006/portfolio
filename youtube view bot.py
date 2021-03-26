from selenium import webdriver
from selenium.webdriver.common.keys import *
import time

link_name = input("input the link : ")
driver = webdriver.Chrome("D:\websearcher\chromedriver")
driver1 = webdriver.Chrome("D:\websearcher\chromedriver")
driver2 = webdriver.Chrome("D:\websearcher\chromedriver")
driver3 = webdriver.Chrome("D:\websearcher\chromedriver")
driver.get(link_name)
driver1.get(link_name)
driver2.get(link_name)
driver3.get(link_name)
for i in range(200):
    driver.get(link_name)
    driver1.get(link_name)
    driver2.get(link_name)
    driver3.get(link_name)
    time.sleep(40)

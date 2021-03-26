from selenium import webdriver
from selenium.webdriver.common.keys import *
currency_type = str(input('what currency do you want to convert?\n: '))
amount_to_convert = int(input('how much to convert?\n: '))
m = webdriver.Chrome("D:\websearcher\chromedriver")
m.get('https://www.google.com/search?q=currency+converter&oq=currenc&aqs=chrome'
      '.1.69i65j0i131i433j69i57j0l4j69i61.4663j1j7&sourceid=chrome&ie=UTF-8')
currency_type.upper()
if currency_type == 'EGP':
    h = m.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[1]/td[1]/input')
    h.send_keys(amount_to_convert)
    y = m.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[1]/td[1]/input')

elif currency_type=='USD':
    h = m.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[1]/td[1]/input')
    h.send_keys(amount_to_convert)
    y = m.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[1]/td[1]/input')

x = [0,1 , 2 , 3, 4, 5]
    ################## NOT COMPLETED , WILL NOT BE COMPLETED ON THIS PATTERN ,  the file is a failure #####################
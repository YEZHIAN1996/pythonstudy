import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test = webdriver.Chrome()
test.maximize_window()
# test.get('https://search.51job.com/list/000000,000000,0000,00,9,99,+,2,1.html')
# print(test.title)
# input = test.find_element(By.ID, 'keywordInput')
# input.send_keys('python')
# button = test.find_element(By.ID, 'search_btn')
# button.click()
# time.sleep(5)

test.get('https://www.baidu.com')
# test.find_element_by_xpath('//input[@id="kw"]').send_keys('python工程师')
# test.find_element_by_xpath('//input[@id="su"]').click()
# time.sleep(2)
# test.get('https://news.baidu.com')
# time.sleep(2)
# test.refresh()
# time.sleep(2)
# test.back()
# time.sleep(2)
# test.forward()
# time.sleep(5)
element = WebDriverWait(test, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
element.send_keys('python')
# above = test.find_element_by_link_text('设置')
# ActionChains(test).move_to_element(above).perform()
time.sleep(5)

test.quit()
from selenium import webdriver
from pprint import pprint

chrome_driver_path = "C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.tet)

# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute('placeholder'))
#
# logo = driver.find_element_by_class_name('python-logo')
#
# documentation_link = driver.find_element_by_css_selector('.documentation-widget a')
# print(documentation_link.text)

# xpath_element = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[3]/b')
# print(xpath_element.text)

event_dates = driver.find_elements_by_css_selector('.event-widget time')
event_names = driver.find_elements_by_css_selector('.event-widget li a')
events = {n: {'date': event_dates[n].text, 'name': event_names[n].text} for n in range(len(event_dates))}
print(events)
driver.quit()

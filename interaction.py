from selenium import webdriver
import time

chrome_driver_path = "C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

big_cookie = driver.find_element_by_id('cookie')


def buy_gadget():
    # get updated price.
    gadgets_list = driver.find_elements_by_css_selector('#store div')

    gadget_price = []

    for gadget in gadgets_list:
        if gadget.text != "" and len(gadget.text.split('-')) > 1:
            item = gadget.text.split('-')
            price = int(item[1].split()[0].strip().replace(',', ''))
            gadget_price.append({'id': gadget.get_attribute('id'), 'price': price})

    print(gadget_price)
    our_money = driver.find_element_by_id('money').text.replace(',', '')

    available_cookies = int(our_money)

    # purchase the gadget with the highest price
    # to do that, we compare the cookies we have vs the price of gadgets
    # if one gadget is <= our cookies number but highest among the price, buy it
    highest_available = gadget_price[0]

    for gadget in gadget_price:
        if highest_available['price'] < gadget['price'] < available_cookies:
            highest_available = gadget

    gadget_to_buy = driver.find_element_by_id(highest_available['id'])
    gadget_to_buy.click()


timeout = time.time() + 5
restart_time = time.time() + 60 * 5

while True:

    big_cookie.click()

    if time.time() > timeout:
        # buy affordable gadget
        buy_gadget()
        timeout = time.time() + 5

    if time.time() > restart_time:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break


driver.quit()
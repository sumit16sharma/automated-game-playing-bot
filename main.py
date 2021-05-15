from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = "D:\Sumit\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

timeout = time.time() + 60*300

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

# number_of_products_unlocked = driver.find_elements_by_class_name("unlocked")
# print(number_of_products_unlocked)
five_second = time.time() + 60*0.083

while True:
    cookie.click()
    count = int(cookie_count.text.split(" ")[0])
    if time.time() > five_second:
        condition = True
        for item in items:
            value = int(item.text)
            if count >= value and condition:
                upgrade_action = ActionChains(driver)
                upgrade_action.move_to_element(item)
                upgrade_action.click()
                upgrade_action.perform()
                five_second = time.time() + 60 * 0.083
                condition = False

    if time.time() > timeout:
        break



# we are going to try to use mouse ActionChains (drag, drop, etc.) in this project where we play the cookie game.
# (no this is not about browser cookies). The game involves clicking a cookie to gain points and using the points to buy items from
# the game store. We are going to develop a script that clicks the cookie just enough to get the points required to buy the items.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/mnt/d/web_dev/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')
actions = ActionChains(driver)

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        val = int(item.text)
        if val <= count:
            upgrade_act = ActionChains(driver)
            upgrade_act.move_to_element(item)
            upgrade_act.click()
            upgrade_act.perform()

# this is the 3rd program in the selenium_intro series where we include actions such as clicking certain button based on their
# attributes. We also tried moving backward and forward in the webpages using the respective functions.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/mnt/d/web_dev/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net/')

link = driver.find_element_by_link_text("Python Programming")
link.click()

# the try-except block makes the webdriver wait awhile till the "main" id block
# is loaded so that we dont encounter errors due to the python code running faster than the webpage can load.
try:
    element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Intermediate Python Tutorials")
    ))
    element1.click()

    element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "sow-button-19310003")
    ))
    element2.click()
    for i in range(3):
        driver.back()

    # driver.forward() # this also exists
except:
    driver.quit()

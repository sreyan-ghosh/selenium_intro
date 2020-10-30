# this is the first file in the selenium intro directory. Here we establish a connection with the website, enter a value
# into the search bar and query the website for results and print the main content of the results page.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/mnt/d/web_dev/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net/')
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys('django')
search.send_keys(Keys.RETURN)

# print(driver.page_source) # returns the entire source code for the HTML page you are visiting
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")) # the try-except block makes the webdriver wait awhile till the 
    )                                                   # "main" id block is loaded so that we dont encounter errors due to the 
    print(main.text)                                    # the python code running faster than the webpage can load.
except:
    driver.quit()


driver.quit()
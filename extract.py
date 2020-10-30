# This is the second file of the selenium series. Here we perform the same actions as the first file but go deeper to 
# extract information from specific tags and class names.

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

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))     # the try-except block makes the webdriver wait awhile till the 
    )                                                       # "main" id block is loaded so that we dont encounter errors due to the 
    articles = main.find_elements_by_tag_name("article")    # the python code running faster than the webpage can load.
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print('\n\n' + header.text)

finally:
    driver.quit()
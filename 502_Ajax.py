#############
### Solved By Sleeping, which is lack of efficiency and could have caused problems if the scraping is going big
###########


from selenium import webdriver
import time


ajaxUrl = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantomJSPath)
driver.get(ajaxUrl)

time.sleep(3)

print(driver.find_element_by_id("content").text)
driver.close()


#############
### Using BS4
########

from bs4 import BeautifulSoup
driver = webdriver.PhantomJS(executable_path=phantomJSPath)
driver.get(ajaxUrl)
time.sleep(3)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.find(id="content").get_text())
driver.close()


##################
### Advanced
################

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path=phantomJSPath)
driver.get(ajaxUrl)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loadedButton")))
    ## By.ID AKA : find_element_by_id
    ## Other options would be like By.ClASSNAME, By.CSS_SELECTOR ...
finally:
    print(driver.find_element_by_id("content").text)
driver.close()
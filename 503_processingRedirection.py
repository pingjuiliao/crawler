from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time
phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
def waitForLoad(driver) :
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count> 20 :
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try: 
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return
        
driver = webdriver.PhantomJS(executable_path= phantomJSPath)
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
###########
### Get cookies
#########

phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path= phantomJSPath)
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

#############
### Other operations
###########
savedCookies = driver.get_cookies()
driver2 = webdriver.PhantomJS(executable_path = phantomJSPath)
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()
# driver2.refresh()
#add this line cause error :(
print(driver2.get_cookies())

for cookie in savedCookies:
    try:
        driver2.add_cookie(cookie)
    except WebDriverException: 
        print("Unable to set Cookie :" + str(cookie))


driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver2.get_cookies())
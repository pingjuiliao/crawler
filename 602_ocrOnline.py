import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

##########
## Not working
########

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import psyco
# psyco.full()


phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"

driver = webdriver.PhantomJS(executable_path = phantomJSPath)
# driver = webdriver.Firefox(executable_path = "../../../usr/bin/firefox")
driver.set_window_size(1124, 850)
driver.get("https://www.amazon.com/Crime-Punishment-Fyodor-Dostoyevsky/dp/0486415872/ref=pd_sim_14_1?_encoding=UTF8&psc=1&refRID=X48GKG0Z2HVDV5JJA1EV")
time.sleep(2)

# Click the "browsing" button
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

## Loading the web page
time.sleep(5)


print("start while")
# i = 100
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style") :
    # print("in while")
    
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    
    ## Get the page loaded
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    #### : ( the page has been changed
    # print(pages)
    for page in pages :
        image = page.get_attribute("src")
        imageList.add(image)

    
driver.quit()

## Start using Tesseract
print("jello")
for image in sorted(imageList) :
    # print("in for loop")
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], \
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    # print("p.wait()")
    f = open("page.txt", "r")
    print(f.read())

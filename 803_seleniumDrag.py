from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"

driver = webdriver.PhantomJS(executable_path = phantomJSPath)
driver.get("http://pythonscraping.com/pages/javascript/draggableDemo.html")
driver.set_window_size(1124, 850)

print(driver.find_element_by_id("message").text)
elementContainer = driver.find_element_by_id("div1")
element = driver.find_element_by_id("draggable")
# print(element.get_attribute("class"))
target = driver.find_element_by_id("div2")
# print(target.get_attribute("class"))

actions = ActionChains(driver)
actions.move_to_element(elementContainer)
# actions.drag_and_drop_by_offset(element, 0, 100).perform()
actions.drag_and_drop(element, target)
actions.click_and_hold(element)
actions.release(target)
actions.perform()
print(driver.find_element_by_id("message").text)
print(driver.find_element_by_tag_name("body").get_attribute("style"))
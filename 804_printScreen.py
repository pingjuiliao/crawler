from selenium import webdriver
phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path = phantomJSPath)
driver.set_window_size(1124, 850)
driver.get("http://www.pythonscraping.com/")
driver.get_screenshot_as_file("screenshot.png")
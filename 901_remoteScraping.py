#############
### Tor(the Onion Router) and Pysocks
###########

import socks
import socket
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://icanhazip.com"
html = urlopen('http://icanhazip.com')
print("original ip address :" + str(html.read()))

# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket

# urlopen('http://icanhazip.com').read()
# print(html.read())
# # bsObj = BeautifulSoup(html)

from selenium import webdriver
service_args = ['--proxy=localhost:9150', '--proxy-type=socks5']
phantomJSPath = "phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantomJSPath, service_args=service_args)
driver.get(url)
print(driver.page_source)
driver.close()
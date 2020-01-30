from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

##
### This program crawl over the whole website and print the stuff on every page.
##

pages = set()

def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html)
	try:
		print(bsObj.h1.get_text())
		print(bsObj.find(id = "mw-content-text").findAll("p")[0])
		print(bsObj.find(id = "ca-edit").find("span").find("a").attrs["href"])
	except AttributeError:
		## missing sth
		print("This page is missing something!!!!")

	for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print("current page : " + pageUrl)
				print("------------\n" + newPage)
				pages.add(newPage)
				getLinks(newPage)


getLinks("")
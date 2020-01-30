from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

####
##### This crawler crawl over rand
####


#########
# Recursive crawler which repeatly visit the same pages
######

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org" + articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div", {"id": "bodyContent"}).findAll(
		"a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0 :
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)
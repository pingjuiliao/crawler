from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


###
#### This program get all External LINKS of a single website
### 

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinksOf(bsObj, includeUrl):
	internalLinks = []
	includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
	print("includeUrl is "+ includeUrl)
	#Finds all links that begin with a "/"
	for link in bsObj.findAll("a", href= re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None :
			if link.attrs['href'] not in internalLinks:
				## Handle URL
				if link.attrs['href'].startswith("//") :
					continue
				elif link.attrs['href'].startswith('/') :
					internalLinks.append(includeUrl+link.attrs['href'])
				else :
					internalLinks.append(link.attrs['href'])
	return internalLinks

def getExternalLinksOf(bsObj, excludeUrl):
	externalLinks = []
	for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")
	# print("addressParts is " + str(addressParts))
	return addressParts

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html)
	externalLinks = getExternalLinksOf(bsObj, urlparse(startingPage).netloc)
											  ##############################
	if len(externalLinks) == 0 :
		print("No external Links ! Look around the site for one")
		domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc	
		#print("domain is " + domain)
		internalLinks = getInternalLinksOf(bsObj, domain)
		return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
	else :
		return externalLinks[random.randint(0, len(externalLinks)-1)]


def randomllyFollowExternalOnly(startingSite): 
	externalLink = getRandomExternalLink(startingSite)
	print("Random External Links is")
	randomllyFollowExternalOnly(externalLink)


######
#### Advance : getAllExternalLinks
######

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl) : 
	
	html = urlopen(siteUrl)
	domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
	bsObj = BeautifulSoup(html,"html.parser")
	print(splitAddress(siteUrl))
	internalLinks = getInternalLinksOf(bsObj, domain)
	externalLinks = getExternalLinksOf(bsObj, domain)

	#print("internalLinks is ###########################")
	#print(internalLinks)

	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print("About to get link: " + link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

targetWebsite = "http://oreilly.com"
allIntLinks.add(targetWebsite)
	## randomllyFollowExternalOnly(targetWebsite)
getAllExternalLinks(targetWebsite)




from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup
import unittest
import re
import datetime
import random

class TestWikipedia(unittest.TestCase) :
    bsObj = None
    url = None
    def test_PageProperties(self) :
        print("###########test_PageProperties###########")
        global bsObj
        global url
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        
        # Test first 100 web pages
        for i in range(1, 100) :
            bsObj = BeautifulSoup(urlopen(url), "html5lib")
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
            
    def titleMatchesURL(self) :
        # print("###########titleMatchesURL##########")
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_","")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]
    
    def contentExists(self) :
        # print("##########contentExists##########")
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False
    
    def getNextLink(self) :
        global bsObj
        random.seed(datetime.datetime.now())
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        return links[random.randint(0, len(links)-1)].attrs["href"]
    # def setUpClass():
    #     print("##########setupClass##########")
    #     global bsObj
    #     url = "http://en.wikipedia.org/wiki/Monty_Python"
    #     bsObj = BeautifulSoup(urlopen(url), "html5lib")
    # def test_titleText(self):
    #     print("##########test_titleText##########")
    #     global bsObj
    #     pageTitle = bsObj.find("h1").get_text()
    #     self.assertEqual("Monty Python", pageTitle)
    # def test_contentExists(self):
    #     print("#########contentExists###########")
    #     global bsObj
    #     content = bsObj.find("div",{"id": "mw-content-text"})
    #     self.assertIsNotNone(content)
    # def test_nothing(self) :
    #     print("this function test nothing")


if __name__ == '__main__' :
    unittest.main()
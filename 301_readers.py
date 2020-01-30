
## TXT
from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())

textPage2 = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textPage2.read(), 'utf-8')

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")

## CSV
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
##　Alternative : csv.DictReader
print("HERE COMES THE CSV OUTPUT !!!!!!!!!!!!!!!!!!") 
for row in csvReader:
    # print(row)
    print("The album \"" + row[0] + "\" was released in " + str(row[1]))
    
    
## PDF
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile) :
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams= laparams)
    
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    
    content = retstr.getvalue()
    retstr.close()
    return content
    
print("HERE COMES THE PDF OUTPUT !!!!!!!!!!!!!!!!!!")    
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()


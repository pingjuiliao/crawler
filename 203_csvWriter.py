import csv 

# csvFile = open("../files/test.csv", 'w+', newline='')
# try : 
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10) :
#         writer.writerow( (i, i+2, i*2))
# finally:
#     csvFile.close()
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

if not os.path.exists("files") :
    os.makedirs("files")
csvFile = open("files/editors.csv", 'wt', newline='', encoding= 'utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
                                ########
        writer.writerow(csvRow)
finally:
    csvFile.close()
    
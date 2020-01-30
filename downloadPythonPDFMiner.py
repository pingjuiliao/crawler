from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os

# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory) :
#     path = absoluteUrl.replace("www.", "")
#     path = path.replace(baseUrl, "")
#     path = downloadDirectory + path
#     directory = os.path.dirname(path)
    
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     return path
absoluteUrl = "https://pypi.python.org/packages/8c/87/cee0aa24f95c287020df7e3936cb51d32b34b05b430759bac15f89ea5ac2/pdfminer3k-1.3.1.tar.gz"
fname = "./packages/pdfminer3k.tar.gz"
html = urlopen(absoluteUrl)
# bsObj = BeautifulSoup(html)
if not os.path.exists("packages") :
    os.makedirs("packages")
if not os.path.exists("packages/pdfminer3k.tar.gz") :
    # print("the file hasn't been downloaded !")
    urlretrieve(absoluteUrl, fname)

###########
###  Unzip
##########

import tarfile

if (fname.endswith("tar.gz")):
    if not os.path.exists("pdfminer3k-1.3.1") :
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    
elif (fname.endswith("tar")):
    tar = tarfile.open(fname, "r:")
    tar.extractall()
    tar.close()


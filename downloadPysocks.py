from urllib.request import urlopen, urlretrieve
import os
absoluteUrl = "https://pypi.python.org/packages/88/ea/36977f21a6f2348237f6fae65090330b02e77fc64d04574eb711a06a4a94/PySocks-1.5.0.tar.gz"
filename = "PySocks-1.5.0.tar.gz"
html = urlopen(absoluteUrl)
if not os.path.exists("packages") :
    os.path.makedirs("packages")
filepath = "./packages/" + filename
if not os.path.exists(filepath) :
    urlretrieve(absoluteUrl, filepath)

import tarfile

unpackedPackageName = "PySocks-1.5.0"
if (filepath.endswith("tar.gz")):
    if not os.path.exists(unpackedPackageName) :
        tar = tarfile.open(filepath, "r:gz")
        tar.extractall()
        tar.close()
    
elif (filepath.endswith("tar")):
    tar = tarfile.open(filepath, "r:")
    tar.extractall()
    tar.close()

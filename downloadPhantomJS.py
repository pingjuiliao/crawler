import os

from urllib.request import urlretrieve
downloadUrl = "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2"
filename = "phantomjs.tar.bz2"
filepath = "packages/"+filename
if not os.path.exists(filepath):
    urlretrieve(downloadUrl, filepath)
    
    
import tarfile

if (filepath.endswith("tar.bz2")):
    if not os.path.exists("phantomjs-2.1.1") :
        tar = tarfile.open(filepath, "r:bz2")
        tar.extractall()
        tar.close()
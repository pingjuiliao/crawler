from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

##################
### Basic Version
##################

printNumber = 10

def cleanInput(input) :
    input = re.sub('\n+', " ", input)
    input = re.sub('[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii","ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input :
        item = item.strip(string.punctuation)
                            ################
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i') :
            cleanInput.append(item)
    return cleanInput    

def getNgrams_basicVersion(input, n) :
    # input = input.split(' ')
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1) :
        output.append(input[i:i+n])
    return output
    
#
## Basic version 
basic_html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
basic_bsObj = BeautifulSoup(basic_html)
basicContent = basic_bsObj.find("div", {"id": "mw-content-text"}).get_text()
basicNgrams = getNgrams_basicVersion(basicContent, 2)
print(basicNgrams)
print("2grams count is" + str(len(basicNgrams)))


##################
### Advance Version
##################

def getNgrams(input, n) :
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1) :
        ngramTemp = " ".join(input[i: i+n])
        if ngramTemp not in output :
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output
    
content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = getNgrams(content, 2)
sortedGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse= True)
print(sortedGrams[:printNumber])


##################
### ultimate version
##################

def isCommon(ngram) :
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", \
                    "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", \
                    "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", \
                    "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", \
                    "if", "would", "her", "all", "my", "make", "about", "know", "will", \
                    "as", "up", "one", "time", "has", "been", "there", "year", "so", \
                    "think", "when", "which", "them", "some", "me", "people", "take", \
                    "out", "into", "just", "see", "him", "your", "come", "could", "now", \
                    "than", "like", "other", "how", "then", "its", "our", "two", "more", \
                    "day", "more", "use", "no", "man", "find", "here", "thing", "give", \
                    "many", "well"]
    for word in ngram :
        if word in commonWords:
            return True
    return False

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = getNgrams(content, 2)
for ngram in ngrams.keys() :
    if isCommon(ngram.split(" ")) :
        ngrams[ngram] = 0
sortedGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse= True)
print(sortedGrams[:printNumber])
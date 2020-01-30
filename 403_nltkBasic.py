


# from nltk import download
# download("gutenberg")
# download("inaugural")
# download("nps_chat")
# download("webtext")
# download("treebank")
# download("punkt")
# download("book")


from nltk.book import *
from nltk import word_tokenize
text = word_tokenize("Strange women lying in ponds distributing swords is no" \
                 + " basis for a system of government. Supreme executive power derives" \
                 + " from a mandate form the masses, not from some farcical aquatic ceremony")
from nltk import pos_tag

print(pos_tag(text))

print("Tokenize 2")
text2 = word_tokenize("The dust was thick so he had to dust")
print(pos_tag(text2))



################
### NLTK Simple Training
########

from nltk import sent_tokenize
sentences = sent_tokenize("Google is one of the best companies in the world" + \
                            " I constantly google myself to see what I'm up to.")
nouns = ['NN', 'NNS', 'NNP', 'NNPS']
for sentence in sentences :
    if "google" in sentence.lower() :
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == "google" and word[1] in nouns :
                print(sentence)
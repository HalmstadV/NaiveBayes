import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import string
datasetLineCount = sum(1 for line in open('imdb_dataset.txt'))
dictionaryLineCount = sum(1 for line in open('dictionary.txt'))
stopwordsLineCount = sum(1 for line in open('stopwords.txt'))
removePunctuation = str.maketrans('', '', string.punctuation)
stopWordList = list()
dictionary = {}

try:
    filename = "dictionary.txt"
    f = open(filename, "r+")

    filename2 = "stopwords.txt"
    f2 = open(filename2,"r+")
except IOError:
    print("Can't find files")






#Construct Sentiment Dictionary

try:
    for i in range(dictionaryLineCount):
        dictionaryline = f.readline()
        splitted_line = dictionaryline.split()

        word=splitted_line[2].replace("word1=","")
        value=splitted_line[splitted_line.__len__()-1].replace("priorpolarity=","")
        dictionary[word] = value
except IOError:
    f.close()

#Construct Stop Word List
for i in range(stopwordsLineCount):
    stopwordline = f2.readline().replace("\n", "")
    stopWordList.append(stopwordline)


try:
    #Read file,apply text preprocessing and write the preprocessed file into a new text file
    file1 = open("imdb_dataset.txt","r")
    appendFile = open("filteredtext.txt", "w")
    for i in range(datasetLineCount):

        datasetline = file1.readline().lower().translate(removePunctuation)

        words = datasetline.split()
        filteredList = []
        for r in words:
            if r not in stopWordList:
                filteredList.append(r)

        stringLine = " ".join(filteredList)
        appendFile.write("{}\n".format(stringLine))

except IOError:
    appendFile.close()




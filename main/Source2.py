import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

removePunctuation = str.maketrans('', '', string.punctuation)
stopWordList = list()
dictionary = {}

filename = "dictionary.txt"
f = open(filename, "r+")


filename2 = "stopwords.txt"
f2 = open(filename2,"r+")





#Construct Sentiment Dictionary

for i in range(8222):
    dictionaryline = f.readline()
    # print(line)
    splitted_line = dictionaryline.split()

    word=splitted_line[2].replace("word1=","")
    value=splitted_line[splitted_line.__len__()-1].replace("priorpolarity=","")
    dictionary[word]=value

#Construct Stop Word List
for i in range(173):
    stopwordline = f2.readline().replace("\n", "")
    stopWordList.append(stopwordline)


#Read file,apply text preprocessing and write the preprocessed file into a new text file
file1 = open("imdb_dataset.txt","r")
appendFile = open("filteredtext.txt", "w")
for i in range(1000):

    datasetline = file1.readline().lower().translate(removePunctuation)

    words = datasetline.split()
    filteredList = []
    for r in words:
        if r not in stopWordList:
            filteredList.append(r)

    stringLine = " ".join(filteredList)
    appendFile.write("{}\n".format(stringLine))

appendFile.close()




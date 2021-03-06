
import string

yelp_datasetDirectory = '..\\text_files\\yelp_dataset.txt'
imdb_datasetDirectory = '..\\text_files\\imdb_dataset.txt'
amazon_datasetDirectory = '..\\text_files\\yelp_dataset.txt'


datasetLineCount = sum(1 for line in open(amazon_datasetDirectory))
dictionaryLineCount = sum(1 for line in open('dictionary.txt'))
stopwordsLineCount = sum(1 for line in open('stopwords.txt'))

removePunctuation = str.maketrans('', '', string.punctuation)
stopWordList = list()
dictionary = {}


firstSentenceScores = list()
analysedSentenceScores = list()



#Dictionary

#Stop Words


def sentimentAnalyze(filename,**dictionary):

    textfile = open(filename,"r")
    for i in range(1000):
        positiveWordCount = 0;
        negativeWordCount = 0;
        sentenceSentimentScore = 0;
        string3 = textfile.readline()
        splitted_line = string3.split()

        #pre-processed sentence
        for word in splitted_line:
            stringLine = " ".join(splitted_line)
            if word in dictionary:
                word_sentiment = dictionary.get(word,"None")
                if word_sentiment.__eq__("positive"):
                    positiveWordCount+= 1
                elif word_sentiment.__eq__("negative"):
                    negativeWordCount+=1



        if positiveWordCount==0 and negativeWordCount==0:
            sentenceSentimentScore=-0
            analysedSentenceScores.append("0")
        elif positiveWordCount>negativeWordCount:
            sentenceSentimentScore=1
            analysedSentenceScores.append("1")
        elif negativeWordCount>positiveWordCount:
            sentenceSentimentScore=0
            analysedSentenceScores.append("0")
        elif positiveWordCount==negativeWordCount:
            sentenceSentimentScore=0
            analysedSentenceScores.append("0")

        # print( stringLine+ " -  Negative word count : {} , Positive word count {}".format(negativeWordCount,
        #                                                                                  positiveWordCount))

        # print( stringLine +" Sentence Score : {}  ".format(sentenceSentimentScore))
    # print(analysedSentenceScores)

def constructDictionary(filename,dictionary):
    f = open(filename, "r+")

    for i in range(dictionaryLineCount):
        dictionaryline = f.readline()
        splitted_line = dictionaryline.split()

        word=splitted_line[2].replace("word1=","")
        value=splitted_line[splitted_line.__len__()-1].replace("priorpolarity=","")
        dictionary[word] = value

def constructStopWordList(filename, *list):

    f2 = open(filename, "r+")
    # Construct Stop Word List
    for i in range(stopwordsLineCount):
        stopwordline = f2.readline().replace("\n", "")
        stopWordList.append(stopwordline)


constructDictionary("dictionary.txt",dictionary)
constructStopWordList("stopwords.txt",stopWordList)
sentimentAnalyze("..\\text_files\\filteredtext.txt",**dictionary)

#Read file,apply text preprocessing and write the preprocessed file into a new text file

file1 = open("..\\text_files\\imdb_dataset.txt","r")
appendFile = open("..\\text_files\\filteredtext.txt", "w")
ZeroCount = 0;
OneCount = 0;


#Store Original Sentence Scores

for i in range(datasetLineCount):
    datasetline = file1.readline().lower().translate(removePunctuation)
    splitdatasetline = datasetline.split()
    if splitdatasetline[len(splitdatasetline)-1].__contains__("0"):
        firstSentenceScores.append("0")
        ZeroCount+=1
    elif splitdatasetline[len(splitdatasetline)-1].__contains__("1"):
        firstSentenceScores.append("1")
        OneCount+=1
    # datasetline = file1.readline().lower().translate(removePunctuation)


    words = datasetline.split()
    filteredList = []
    for r in words:
        if r not in stopWordList and not r.__contains__("0") and not r.__contains__("1"):
            filteredList.append(r)

    stringLine = " ".join(filteredList)
    appendFile.write("{}\n".format(stringLine))


# print("Number of 0 :{} , Number of 1 : {}".format(ZeroCount,OneCount))



SuccessCount = 0;
FailCount = 0;

for i in range(analysedSentenceScores.__len__()):

    num1 = firstSentenceScores[int(i-1)]
    num2 = analysedSentenceScores[int(i-1)]

    if num1 == num2:
        print("Successful guess")
        SuccessCount+=1

    else:
        print("Failed guess")
        FailCount+=1

    # if analysedSentenceScores[int(i)] is firstSentenceScores[int(i)]:
    #     print("Successful guess")
    #     SuccessCount+=1
    # elif analysedSentenceScores[int(i)] is not firstSentenceScores[int(i)]:
    #     print("Failed guess")
    #     FailCount+=1


print("No Successful Guesses : {} ".format(SuccessCount))
print("No Failed Guesses : {}".format(FailCount))

print(len(analysedSentenceScores))
print(len(firstSentenceScores))



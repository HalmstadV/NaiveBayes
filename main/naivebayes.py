import csv
import string

imdblocation = "..//text_files//imdb_dataset.csv"
yelplocation = "..//text_files//yelp_dataset3.csv"
amazonlocation = "..//text_files//amazon_dataset3.csv"
amazonyelplocation = "..//text_files//amazon_yelp_combined.csv"


trainlocation = imdblocation
testlocation = amazonlocation

removePunctuation = str.maketrans('', '', string.punctuation)

sentences = list()
sentence_predictions = list()

words = {}
negprob = {}
posprob = {}

def read_and_store_sentences_in_list(list,trainlocation):
    with open(trainlocation, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        for line in csv_reader:
            sentence = str(line[0]).lower().split(" ")
            sentence_sentiment = str(line[1])

            # sentence2 =[str(line).lower().split(" ") for line in csv_reader]

            last_string = " ".join(sentence).translate(removePunctuation).casefold()

            list.append(last_string)
            list.append(sentence_sentiment)


#test trained naive bayes classifier and report accuracy

def testNaiveBayes(testlocation,**dictionary):
    with open(testlocation, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        successful_predictions = 0
        failed_predictions = 0
        index = 0

        for line in csv_reader:
            negative_score = 0
            positive_score = 0

            sentence = str(line[0]).lower().split(" ")
            sentence_sentiment = str(line[len(line) - 1])

            for item in sentence:
                if item.casefold() in words:
                    negative_score += negprob[item]
                    positive_score += posprob[item]
                else:
                    negative_score += float(1 / len(words)+10)
                    positive_score += float(1 / len(words)+10)

            returnmax_and_store(sentence_predictions, number1=positive_score, number2=negative_score)

            if sentence_predictions[index] is sentence_sentiment:
                successful_predictions += 1
            else:
                failed_predictions += 1

            index += 1

            print(
                str(line) + "prob of 0 : " + str(negative_score)[0:4] + " " + "prob of 1 : " + str(positive_score)[0:4])
            print("Success : {} Fail {} ".format(successful_predictions, failed_predictions))


#take max value of a sentence score and store it in list

def returnmax_and_store(list1, number1, number2):


    if max(number1, number2) is number1:
        list1.append("1")
    else:
        list1.append("0")




def calculate_likelihoods(**words):

    # For every word in dataset,calculate the positive and
    # negative occurences for each word

    for word in words:
        pos_occurence = str(words[word]['1_counts'])
        neg_occurence = str(words[word]['0_counts'])
        # print("{} pos : {} , neg : {}".format(word,pos_occurence,neg_occurence))

        negprob[word] = float(int(neg_occurence) / (int(neg_occurence) + int(pos_occurence)))
        posprob[word] = float(int(pos_occurence) / (int(pos_occurence) + int(neg_occurence)))

        # print("word neg : "  + word + str(negprob[word]))
        # print("word pos: " + word +str(posprob[word]))


def calculate_word_frequencies(trainlocation,dictionary):

    with open(trainlocation, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        for line in csv_reader:
            sentence = str(line[0]).lower().split(" ")

            sentence_sentiment = str(line[1])
            for word in sentence:

                if not word in dictionary:
                    dictionary[word] = {'0_counts': 0, '1_counts': 0}
                dictionary[word][str(sentence_sentiment) + '_counts'] += 1

        # for i in words:
        #     print(i, words[i])
        #




def main():
    read_and_store_sentences_in_list(sentences, trainlocation=trainlocation)
    calculate_word_frequencies(trainlocation, words)
    calculate_likelihoods(**words)
    testNaiveBayes(yelplocation, **words)




main()

# with open(trainlocation, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#
#
#     for line in csv_reader:
#         sentence = str(line[0]).lower().split(" ")
#
#         sentence_sentiment = str(line[1])
#         for word in sentence:
#
#             if not word in words:
#                 words[word] = {'0_counts': 0, '1_counts': 0}
#             words[word][str(sentence_sentiment) + '_counts'] += 1
#
#     # for i in words:
#     #     print(i, words[i])
#     #



#Initialize dictionaries for probabilities








# with open(testlocation, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#
#     successful_predictions = 0
#     failed_predictions = 0
#     index = 0
#
#
#     for line in csv_reader:
#         negative_score = 0
#         positive_score = 0
#
#         sentence = str(line[0]).lower().split(" ")
#         sentence_sentiment = str(line[len(line) - 1])
#
#         for item in sentence:
#             if item.casefold() in words:
#                 negative_score += negprob[item]
#                 positive_score += posprob[item]
#             else:
#                 negative_score += float(1 / len(words))
#                 positive_score += float(1 / len(words))
#
#         returnmax_and_store(sentence_predictions,number1=positive_score, number2=negative_score)
#
#         if sentence_predictions[index] is sentence_sentiment:
#             successful_predictions += 1
#         else:
#             failed_predictions += 1
#
#         index += 1
#
#
#         print(str(line) + "prob of 0 : " + str(negative_score)[0:4] + " " + "prob of 1 : " + str(positive_score)[0:4])
#         print("Success : {} Fail {} ".format(successful_predictions, failed_predictions))






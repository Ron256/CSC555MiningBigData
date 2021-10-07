def readFile(fileName):
        """Function that returns a list of words after reading a file"""
        bagOfWordsL = []
        with open(fileName) as f:
                # read the file and generate a list of strings
                lines = f.readlines()

                for i in range(len(lines)):
                        # a list of words is created by splitting the string
                        splittedWordsL = lines[i].split(' ')

                        # loop through the list of words and add words to the bag of words list
                        for splittedItem in range(len(splittedWordsL)):
                                # if there are any empty spaces just pass
                                if len(splittedWordsL[splittedItem]) == 0:
                                        pass
                                else:
                                        # used a replace function to  remove all line breaks.
                                        bagOfWordsL.append(splittedWordsL[splittedItem].replace('\n',''))

        return bagOfWordsL      # return a list of bag of words.


def wordCnt(listOfWords):
    """Function that generates a dictionary of words with their frequency of occurance"""
    wordCnt = {}                                                                                        # define an empty dictionary
    for i in range(len(listOfWords)):                                                                   # iterate through the list of words and count the number of words
        if listOfWords[i] in wordCnt.keys():
            wordCnt[listOfWords[i]] = wordCnt[listOfWords[i]] + 1
        else:
            wordCnt[listOfWords[i]] = 1
    return wordCnt                                                                                      # return a dictionary of the different  words with their frequencies.

listOfBagOfWords = readFile('myfile.txt')                                                               # return a list of words
wordsCntDict = wordCnt(listOfBagOfWords)                                                                # uses a helper function that returns  a dictionary of  the different words with their frequencies

# sort the dictionary
sortedWordCntDict = {key: value for (key, value) in sorted(wordsCntDict.items(), key=lambda wordCnt: wordCnt[1], reverse = True)}
for key in sortedWordCntDict:
        print('%s %s' %(key, sortedWordCntDict[key]))

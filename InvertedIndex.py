from collections import defaultdict
from email.policy import default
import nltk
import nltk.stem
import os
import json
from bs4 import BeautifulSoup, SoupStrainer
'''
Inverted Index = map with token as key and list of corresponding postings as values
Postings = [document name/id token was found in, tf-idf score (for MS1, add only the term frequency)]
'''

# 50 % ram
# when we hit the threshold
# begin offloading from disk
# ram usage back to 0
# repeat

class InvertedIndex:
    def __init__(self, directory):
        self.map = defaultdict(lambda: defaultdict(int))
        self.dir = directory
        self.docID = 0
        
    # Supplementary querying
    # Milestone #
    def andQuery(self, fL, sL):
        temp = []
        ptrF, ptrS = 0, 0
        n1, n2 = len(fL) - 1, len(sL) - 1
        while ptrF != n1 and ptrS != n2:
            if fL[ptrF] < sL[ptrS]:
                ptrF += 1
            elif fL[ptrF] > sL[ptrS]:
                ptrS += 1
            else:
                temp.append(fL[ptrF])
        return temp

    #Increments the document id to keep track of current file
    def incrementID(self):
        self.docID += 1

    #
    def indexFiles(self):
        print("INDEXING")
        for folderName in os.listdir(self.dir):
            folder = os.path.join(self.dir, folderName)
            self.processFolder(folder)
            break
    
    def processFolder(self, folderPath):
        print("FOLDER PATH: " + folderPath)
        for fileName in os.listdir(folderPath):
            filePath = os.path.join(folderPath, fileName)
            self.processFile(filePath)
            break
    
    def processFile(self, filePath):
        print("FILE PATH: " + filePath)
        with open(filePath, "r") as file:
            loadedFile = json.load(file)
            # url = loadedFile["url"]
            content = loadedFile["content"]
            # encoding = loadedFile["encoding"]
            tokenList = self.tokenizeContent(content)
            # self.computeWordDoc(tokenList)
            
    def tokenizeContent(self, content):
        stemmer = nltk.stem.snowball.EnglishStemmer()
        content = BeautifulSoup(content, "lxml").get_text()
        tokens = []
        matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"
        content_list = content.split('\n')
        for line in content_list:
            finStr = ""
            i = 0
            for chars in line:
                if not(chars in matchString):
                    chars = ' '
                    if finStr and i and finStr[i-1] == ' ':
                        chars = ''
                        i -= 1
                finStr += chars
                i += 1
            if finStr:
                for string in [s.lower() for s in finStr.split()]: #lowrcase strings in split
                    if string.isalpha():
                        string = stemmer.stem(string)
                    tokens.append(string)
        print(tokens)
        return tokens

    def computeWordDoc(self, tokenizedList):
        temp = {values:self.docID for values in tokenizedList}
        self.incrementID()
        return temp

    def updateMap(self, tempMap):
        for k in tempMap.keys():
            for nk in tempMap[k]:
                self.map[k][nk] += tempMap[k].get(nk, 0)
  
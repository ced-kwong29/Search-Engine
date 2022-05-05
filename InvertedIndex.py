from collections import defaultdict
from email.policy import default
import nltk
import nltk.stem
import os
import json
from bs4 import BeautifulSoup, SoupStrainer
import psutil
'''
Inverted Index = map with token as key and list of corresponding postings as values
Postings = [document name/id token was found in, tf-idf score (for MS1, add only the term frequency)]
'''


class InvertedIndex:
    def __init__(self, directory):
        self.map = defaultdict(lambda: defaultdict(int))
        self.dir = directory
        self.docID = 0
        self.merge_counter = 1
        self.memory_limit = .8
        self.counter = 0
        self.mergeList = {*{}}      # this is the ONLY way to write a set


    def mergeFiles(self):
        opened_files = [json.loads(json.load(f)) for f in self.mergeList]
        print(opened_files)
        

    def offload(self):
        with open(f"index{self.merge_counter}", "w") as file:
            json.dump(self.map, file)
        self.map = {}
        self.merge_counter += 1


    def checkMemoryUsage(self):
        return psutil.virtual_memory()[2]
        

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


    def indexFiles(self):
        print("INDEXING")
        for folderName in os.listdir(self.dir):
            folder = os.path.join(self.dir, folderName)
            self.processFolder(folder)
            if self.counter >= 10:
                break
    

    def processFolder(self, folderPath):
        print("FOLDER PATH: " + folderPath)
        for fileName in os.listdir(folderPath):
            filePath = os.path.join(folderPath, fileName)
            self.processFile(filePath)
            # break
    

    def processFile(self, filePath):
        if self.counter < 10:
            print("FILE PATH: " + filePath)
            with open(filePath, "r") as file:
                loadedFile = json.load(file)
                content = loadedFile["content"]
                memory = self.checkMemoryUsage()
                print("MEMORY: " + str(memory))
                # if memory > self.memory_limit:
                #     self.offload()
                tokenList = self.tokenizeContent(content)
                temp = self.computeWordDoc(tokenList)
                self.updateMap(temp)
                self.counter += 1
        else:
            print(f"{self.counter} files have been read.\n\n")

            
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

    def printMap(self, map):
        for k,v in sorted(map.items()):
            print(k,v)

    def computeWordDoc(self, tokenizedList):
        temp = defaultdict(lambda: defaultdict(int))
        for key in tokenizedList:
            temp[key][self.docID] += 1
        self.incrementID()
        print(temp)
        self.printMap(temp)
        return temp

    def updateMap(self, tempMap):
        for word in tempMap.keys():
            if word not in self.map:
                #print(word + " NOT IN MAP")
                self.map[word] = tempMap[word]
            else:
                for doc in tempMap[word]:
                    self.map[word][doc] = tempMap[word][doc]
        self.printMap(self.map)
        
        
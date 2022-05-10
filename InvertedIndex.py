from collections import defaultdict
from email.policy import default
import nltk
import nltk.stem
import os
import json
from bs4 import BeautifulSoup, SoupStrainer
import psutil
import re

'''
Inverted Index = map with token as key and list of corresponding postings as values
Postings = [document name/id token was found in, tf-idf score (for MS1, add only the term frequency)]
'''


class InvertedIndex:
    def __init__(self, directory):
        self.map = defaultdict(lambda: defaultdict(int))
        self.dir = directory
        self.docID = 0
        self.dump_counter = 1
        self.initial_memory = self.checkMemoryUsage()
        self.memory_limit = .8
        self.foldersVisited = 0
        self.memThreshold = (100 - self.initial_memory) // 3
        self.tbool1, self.tbool2 = True, True
        self.mergeList = []      # this is the ONLY way to write a <crossout>set</crossout> list
        self.wordCounter = 0
        self.dirLength = len(next(os.walk(self.dir))[1]) #also threshold 3
        self.threshold1 = self.dirLength // 3
        self.threshold2 = self.threshold1 * 2
        self.threshold3 = self.dirLength
        self.docDict = {}

        

    def mergeFiles(self):
        opened_files = [json.load((open(f,))) for f in self.mergeList]
        for next_file in opened_files:
            self.mergeMap(self.map, next_file)


    def offload(self):
        name = f"chicken{self.dump_counter}.json"
        with open(name, "w") as file:
            json.dump(self.map, file)
            self.wordCounter += len(self.map.keys())
            self.map = {}
        self.mergeList.append(name)
        self.dump_counter += 1
        self.memThreshold += self.initial_memory // 3
        #print(f"Counter: {self.dump_counter} & Initial memory: {self.initial_memory} & Current memory: {self.checkMemoryUsage()} & File name: {name}")

    #offloads document-map auxilliary structure to disk
    def offloadDocDict(self):
        name = "DocDictionary.json"
        with open(name, "w") as file:
            json.dump(self.docDict, file)


    def checkMemoryUsage(self):
        return psutil.virtual_memory()[2]


    #Increments the document id to keep track of current file
    def incrementID(self):
        self.docID += 1


    def indexFiles(self):
        for folderName in os.listdir(self.dir):
            folder = os.path.join(self.dir, folderName)
            self.processFolder(folder)
        self.offload()          #final offload for after files processed, offloading remaining files past last threshold
        self.mergeFiles()
        self.offloadDocDict() #offloads auxilliary structure holding document urls

        
    def processFolder(self, folderPath):
        print("FOLDER PATH: " + folderPath)
        for fileName in os.listdir(folderPath):
            filePath = os.path.join(folderPath, fileName)
            self.processFile(filePath)
        self.foldersVisited += 1
            
            
    def processFile(self, filePath):
        with open(filePath, "r") as file:
            loadedFile = json.load(file)
            content = loadedFile["content"]
            url = loadedFile["url"]
            self.docDict[self.docID] = url

            if self.tbool1 and (self.foldersVisited >= self.threshold1):
                self.offload()
                self.tbool1 = False
            elif self.tbool2 and (self.foldersVisited >= self.threshold2):
                self.offload()
                self.tbool2 = False
            elif (100 - self.checkMemoryUsage()) >= (self.initial_memory + self.memThreshold):
                self.offload()

            content = BeautifulSoup(content, "lxml").get_text()
            tokenList = self.tokenizeContent(content)
            temp = self.computeWordDoc(tokenList)
            self.updateMap(temp)

        
    def tokenizeContent(self, content):
        stemmer = nltk.stem.snowball.EnglishStemmer()
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
                for strings in [s.lower() for s in finStr.split() if s.isalnum()]:     #lowercase strings in split
                    #if strings not in STOPWORDS:
                    tokens.append(stemmer.stem(strings))
        return tokens


    def printMap(self, map):
        for k,v in sorted(map.items()):
            print(k,v)


    def computeWordDoc(self, tokenizedList):
        temp = defaultdict(lambda: defaultdict(int))
        for key in tokenizedList:
            temp[key][self.docID] += 1
        self.incrementID()
        return temp


    def updateMap(self, tempMap):
        for word in tempMap.keys():
            if word not in self.map:
                self.map[word] = tempMap[word]
            else:
                for doc in tempMap[word]:
                    self.map[word][doc] = tempMap[word][doc]

        
    def mergeMap(self, firstMap, tempMap):
        for word in tempMap.keys():
            if word not in firstMap:
                firstMap[word] = tempMap[word]
            else:
                for doc in tempMap[word]:
                    firstMap[word][doc] = tempMap[word][doc]
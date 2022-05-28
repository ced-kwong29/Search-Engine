from msilib.schema import Directory
from tokenizer import tokenizeContent
import cProfile
import pstats
from collections import defaultdict
# Supplementary querying
# takes in two Lists that contain document IDs for which the word was found in
# returns the intersection of the list
# the 2 words were found to exist in the returned list's documents
# Milestone 2
import cheeseJSON
import json
import math
    
    
class Query:
    def __init__(self, userInput, d):
        self.query = tokenizeContent(userInput)
        self.aux = d #auxiliary index
        self.N = len(set(self.aux.values())) #for calculations regarding tf-idf

    #idf - calculates just the idf, the metric for rarity
    def idf(self, df):
        return math.log((self.N/df))

    #tf - calculates just tf, a normalized metric for term frequency
    def tf(self, df):
        for value in df.values():
            value = 1 + math.log(value)
        return df

        
    def startQuery(self):
        if len(self.query) == 1:
            t = self.singleQuery(self.query[0])
            grabbed_urls = self.grabURLs(t)
            for count, i in enumerate(grabbed_urls):
                if count >= 10:
                    break
                print(i)
        elif len(self.query) >= 2:
            t = self.multipleQuery(self.query)
            grabbed_urls = self.grabURLs(t)
            for count, i in enumerate(grabbed_urls):
                if count >= 10:
                    break
                print(i)
        else:
            print("Invalid input.")
            return

    #grabURLs - matches document IDs with their respective URLs, which are returned to the user
    def grabURLs(self, records):
        with open("DocDictionary.json", 'r') as f:
            temp = json.load(f)
        urls = []
        for values in records:
            t = temp.get(str(values), 0)
            if t:
                urls.append(t)
        return urls


    def andQuery(self, fL, sL): 
        '''
        Performed boolean on two lists, in which both lists must be sorted
        '''
        intersection = []
        ptrF, ptrS = 0, 0
        n1, n2 = len(fL) - 1, len(sL) - 1
        while ptrF < n1 or ptrS < n2:
            if int(fL[ptrF]) < int(sL[ptrS]) and ptrF < n1:
                ptrF += 1
            elif int(fL[ptrF]) > int(sL[ptrS]) and ptrS < n2:
                ptrS += 1
            elif int(fL[ptrF]) == int(sL[ptrS]):
                intersection.append(fL[ptrF])
                if ptrF < n1:
                    ptrF += 1
                if ptrS < n2:
                    ptrS += 1
            elif ptrF == n1 and ptrS < n2:
                ptrS += 1
            elif ptrS == n2 and ptrF < n1:
                ptrF += 1
        return intersection


    def jumpHelper(self, word):
        return cheeseJSON.jumpPos(file, self.aux, word)
        

    #singleQuery - returns documents containing a single word that was queried for
    def singleQuery(self, word):
        aux = self.jumpHelper(word)
        docs = sorted(aux.items(), key=lambda x : -x[1])[:5]
        returnDocs = []
        for doc in docs:
            returnDocs.append(doc[0])
        return returnDocs

    
    def cosineScore(self, cosineD, freqDoc, freqTerm, allDocs, validQueries, lengthDoc):
        scores = []
        if validQueries:
            allDocsInt = [int(i) for i in allDocs] 
            length = [lengthDoc[i] for i in range(max(allDocsInt))]
            scores = [0 for _ in range(max(allDocsInt)+1)]
            for term in validQueries:
                weightTerm = freqTerm[term]
                for doc in allDocsInt:
                    scores[doc] += freqDoc[str(doc)][term] * weightTerm
            for d in range(len(scores)-1):
                if length[d] > 0:
                    scores[d] = math.log(scores[d] / length[d])
        return scores


    def multipleQuery(self, words):
        # initializes the structure to use containing final (intersecting) docs,
        # TF/IDF structures, cosineD which will have
        intersectingDocs = []
        rankingTF = {}
        rankingIDF = {}
        cosineD = {}
        freqTerm = {}
        freqDoc = defaultdict(lambda : defaultdict(int))
        allDocs = set()
        validQueries = []
        lengthDoc = defaultdict(int)
        for word in sorted(words, key=lambda x : -len(x)):
            if len(intersectingDocs) > 1:
                tempD = {}
                firstDoc = intersectingDocs.pop(0)
                secondDoc = intersectingDocs.pop(0)
                tempIntersectingDocs = self.andQuery(list(firstDoc.keys()), list(secondDoc.keys()))
                for doc in tempIntersectingDocs:
                    tempD[doc] = (firstDoc[doc] + secondDoc[doc]) // 2
                intersectingDocs.append(tempD)
            else:
                termFrequencyCurrentWord = self.jumpHelper(word)
                # if the word exists in the inverted index
                if termFrequencyCurrentWord:
                    cosineD[word] = termFrequencyCurrentWord
                    for j in termFrequencyCurrentWord:
                        freqDoc[j][word] = termFrequencyCurrentWord[j]
                        allDocs.add(j)
                        lengthDoc[j] += termFrequencyCurrentWord[j] 
                    validQueries.append(word)
                    freqTerm[word] = sum(termFrequencyCurrentWord.values())
                    intersectingDocs.append(termFrequencyCurrentWord)
                    rankingTF[word] = self.tf(termFrequencyCurrentWord)
                    rankingIDF[word] = self.idf(len(termFrequencyCurrentWord))
        while len(intersectingDocs) > 1:
            tempD = {}
            firstDoc = intersectingDocs.pop(0)
            secondDoc = intersectingDocs.pop(0)
            tempIntersectingDocs = self.andQuery(list(firstDoc.keys()), list(secondDoc.keys()))
            for doc in tempIntersectingDocs:
                tempD[doc] = (firstDoc[doc] + secondDoc[doc]) // 2
            intersectingDocs.append(tempD)
        result = self.cosineScore(cosineD, freqDoc, freqTerm, allDocs, validQueries, lengthDoc)
        finalScore = defaultdict(int)
        docs = []
        if result:
            for k, v in intersectingDocs[0].items():
                temp = result[int(k)]
                if not(temp):
                    temp = 1
                finalScore[int(k)] = math.log(temp / v)
            docs = [i for i, _ in sorted(finalScore.items(), key=lambda x : -x[1])]
        return docs
    

def main(d):
    while True:
        #userInput = input("Search for: ")
        userInput= str(input("Enter your query: "))
        # userInput = 'computer science'
        profiler = cProfile.Profile()
        profiler.enable()
        
        query = Query(userInput, d)
        query.startQuery()
        
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('time')
        # stats.print_stats()

        

    
    
if __name__ == "__main__":
    file = open("InvertedIndex.json")
    d = cheeseJSON.test(file)
    main(d)

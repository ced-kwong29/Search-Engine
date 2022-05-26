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
        self.aux = d
        self.N = len(set(self.aux.values()))

    def idf(self, df):
        return math.log((self.N/df))

    def tf(self, df):
        for value in df.values():
            value = 1 + math.log(value)
        return df

        
    def startQuery(self):
        if len(self.query) == 1:
            t = self.singleQuery(self.query[0])
            self.grabURLs(t)

        elif len(self.query) >= 2:
            t = self.multipleQuery(self.query)
            self.grabURLs(t)
        else:
            print("Invalid input.")
            return

    def grabURLs(self, records):
        with open("DocDictionary.json", 'r') as f:
            temp = json.load(f)
        urls = []
        # print(f"\nTOP {len(records)} for word{'s' if len(self.query) > 1 else ''} {self.query}")
        for values in records:
            t = temp.get(values, 0)
            if t:
                urls.append(t)
                print(t)
        return urls


    def andQuery(self, fL, sL): 
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
        

    def singleQuery(self, word):
        aux = self.jumpHelper(word)
        docs = sorted(aux.items(), key=lambda x : -x[1])[:5]
        returnDocs = []
        for doc in docs:
            returnDocs.append(doc[0])
        return returnDocs
        

    #def tfidf(self, word, doc):
        #tf = 1 + math.log(termFreq)
        #idf = N / docFreq
        #return tf * idf


    def ranking(self, words, tfDict, idfDict):
        #calculate cosine similarity of each doc then return ranking
        #calculate query tfidfs
        qlist = []
        for word in words:
            tf = words.count(word)
            idf = 1 #only one query, appears for this one query
            qlist.append(tf*idf)
        ##now get cosine for each doc
        #gather doc tfidfs for each word
        dlist = []

    
    def cosineScore(self, cosineD, freqDoc, freqTerm, allDocs, validQueries, lengthDoc):
        length = [lengthDoc[i] for i in range(max(allDocs))]
        scores = [0 for _ in range(max(allDocs))]
        for term in validQueries:
            weightTerm = freqTerm[term]
            for doc in allDocs:
                scores[doc] += freqDoc[doc][term] * weightTerm
        for d in range(len(scores)):
            scores[d] /= length[d]
        print(scores)
        return scores


    def multipleQuery(self, words):
        intersectingDocs = []
        rankingTF = {}
        rankingIDF = {}
        cosineD = {}
        freqTerm = {}
        freqDoc = defaultdict(lambda : defaultdict())
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
                curr = self.jumpHelper(word) 
                if curr:
                    cosineD[word] = curr
                    for j in curr:
                        # {'0': {'water':80, 'fire':30}}
                        freqDoc[j][word] = curr[j]
                        allDocs.add(j)
                        lengthDoc[j] += curr[j]

                    validQueries.append(word)
                    freqTerm[word] = sum(curr.values())
                    # {'water':480, 'fire':800}
                    # {'0':40, :'1' 80, '2':30, ...}
                    intersectingDocs.append(curr)
                    rankingTF[word] = self.tf(curr)
                    rankingIDF[word] = self.idf(len(curr))
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
        for k, v in intersectingDocs[0].items():
            finalScore[k] = result[k] / v
        # [{docID#:freq#}, {...}, ...]
        docs = sorted(finalScore.items(), key=lambda x : -x[1])
        return docs
        # return ranking(docs, rankingTF, rankingIDF)
    

def main(d):
    while True:
        
        # userInput = input("Search for: ")
        # if userInput == "q":
        #     break
        # userInput = "The goal of our work is to exploit a distributed power-aware middleware framework to coordinate low-level architectural"
        # userInput = "pool water"
        userInput = "The gaol of our wordk is to expliot a distribbbuted pooper-aware middlewaire framewwwwork to coordinate low-level architectural"
        
        
        profiler = cProfile.Profile()
        profiler.enable()
        
        query = Query(userInput, d)
        query.startQuery()
        
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('time')
        stats.print_stats()
        break
    
    
if __name__ == "__main__":
    file = open("InvertedIndex.json")
    d = cheeseJSON.test(file)
    main(d)
    
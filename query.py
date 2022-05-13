from msilib.schema import Directory
from tokenizer import tokenizeContent

# Supplementary querying
# takes in two Lists that contain document IDs for which the word was found in
# returns the intersection of the list
# the 2 words were found to exist in the returned list's documents
# Milestone 2
import cheeseJSON
    
    
class Query:
    def __init__(self, userInput, d):
        self.query = tokenizeContent(userInput)
        self.aux = d
        
    def startQuery(self):
        if len(self.query) == 1:
            t = self.singleQuery(self.query[0])
            print(t)
        elif len(self.query) >= 2:
            t = self.multipleQuery(self.query)
            print(t)
        else:
            print("Invalid input.")


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
        

    def multipleQuery(self, words):
        intersectingDocs = []
        for word in words:
            if len(intersectingDocs) > 1:
                tempD = {}
                first = intersectingDocs.pop(0)
                second = intersectingDocs.pop(0)
                d = self.andQuery(list(first.keys()), list(second.keys()))
                for values in d:
                    tempD[values] = (first[values] + second[values]) // 2
                intersectingDocs.append(tempD)
            else:
                intersectingDocs.append(self.jumpHelper(word))
        while len(intersectingDocs) > 1:
            tempD = {}
            first = intersectingDocs.pop(0)
            second = intersectingDocs.pop(0)
            d = self.andQuery(list(first.keys()), list(second.keys()))
            for values in d:
                tempD[values] = (first[values] + second[values]) // 2
            intersectingDocs.append(tempD)
        docs = sorted(intersectingDocs[0].items(), key=lambda x : -x[1])[:5]
        returnDocs = []
        for doc in docs:
            returnDocs.append(doc[0])
        return returnDocs
    

def main(d):
    while True:
        userInput = input("Search for: ")
        if userInput == "q":
            break
        query = Query(userInput, d)
        query.startQuery()
    
    
if __name__ == "__main__":
    file = open("II.json")
    d = cheeseJSON.test(file)
    main(d)
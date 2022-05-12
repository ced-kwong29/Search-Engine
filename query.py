from msilib.schema import Directory
from tokenizer import tokenizeContent

# Supplementary querying
# takes in two Lists that contain document IDs for which the word was found in
# returns the intersection of the list
# the 2 words were found to exist in the returned list's documents
# Milestone 2
def andQuery(fL, sL): 
    intersection = []
    ptrF, ptrS = 0, 0
    n1, n2 = len(fL) - 1, len(sL) - 1
    while ptrF != n1 and ptrS != n2:
        if fL[ptrF] < sL[ptrS]:
            ptrF += 1
        elif fL[ptrF] > sL[ptrS]:
            ptrS += 1
        else:
            intersection.append(fL[ptrF])
    return intersection

    # loop through chicken indexes
    #   turn to dictionary
    #       if query is in dictionary
    #           return the dictionary keys associated with the query
    def getDocsWithQuery(self, query):
        pass
    
    
class Query:
    def __init__(self, userInput):
        self.query = tokenizeContent(userInput)
        
    def startQuery(self):
        if len(self.query == 1):
            self.singleQuery()
        elif len(self.query) >= 2:
            self.multipleQuery()
        else:
            print("WEIRD INPUT")
        
    def singleQuery(self):
        print("SINGLE QUERY")
        
    def multipleQuery(self):
        # AND querying
        intersectingDocs = []
        
        
        
    
        
    

def main():
    # userInput = input("ENTER QUERY: ")
    # query = Query(userInput)
    # query.startQuery()
    
    
    

if __name__ == "__main__":
    main()
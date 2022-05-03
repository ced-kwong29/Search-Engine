from collections import defaultdict
from email.policy import default
#import nltk
'''
Inverted Index = map with token as key and list of corresponding postings as values
Postings = [document name/id token was found in, tf-idf score (for MS1, add only the term frequency)]
'''

class InvertedIndex:
    def __init__(self, directory):
        self.map = defaultdict(list)
        self.dir = directory
        
    def indexFiles(self):
        print("INDEXING")
        # open directory
        # loop through all the subfolders in directory 
        # when no subfolders process folder
        #   processFolder()
    
    # def processFolder(self, folderPath):
        # loop through files in folder
        #   processFile()
    
    # def processFile(self, filePath):
        # open file
        # extract content from JSON
        # tokens = tokenizeContent()
        # add tokens to map
        
    # def tokenizeContent(self, content):
        # tokenize content
        # return [tokens]

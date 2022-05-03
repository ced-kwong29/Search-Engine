from collections import defaultdict
from email.policy import default

'''

Inverted Index = map with token as key and list of corresponding postings as values
Postings = [document name/id token was found in, tf-idf score (for MS1, add only the term frequency)]


'''

class InvertedIndex:
    def __init__(self):
        self.map = defaultdict(list)
        # setup index
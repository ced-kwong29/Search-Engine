# rtighiou - 88255446
# wmejiahi - 18183195
# cwkwong -  11234388
# alexanvl - 22558269


from msilib.schema import Directory
from InvertedIndex import InvertedIndex

''' 
Steps:
1. index every file
2. write index to a file system
3. search query in file system
4. show user results               
'''

def main():
    directory = "DEV"
    invertedIndex = InvertedIndex(directory)
    invertedIndex.indexFiles()
    print("HERE ARE THE STATS")
    print("# of docs: " + str(invertedIndex.docID))
    print("# of tokens: " + str(invertedIndex.wordCounter))
    print("DOC DICT: " + str(invertedIndex.docDict))

if __name__ == "__main__":
    main()
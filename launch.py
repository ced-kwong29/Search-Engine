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
    # directory = "developer" #path
    # print("chicken")
    # directory = "C:\Users\Alex\Desktop\search_engine\cs121-search-engine\DEV"
    directory = "DEV"
    invertedIndex = InvertedIndex(directory)
    invertedIndex.indexFiles()
    print("End of program!!!!!!")

if __name__ == "__main__":
    main()
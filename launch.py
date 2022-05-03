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
    directory = "directorypath"
    invertedIndex = InvertedIndex(directory)
    invertedIndex.indexFiles()

    

if __name__ == "__main__":
    main()
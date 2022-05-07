import json



def mergeFiles(testList):
    mapD = {}
    opened_files = [json.load((open(f,))) for f in testList]
    for next_file in opened_files:
        mergeMap(mapD, next_file)
    
def mergeMap(firstMap, tempMap):
    for word in tempMap.keys():
        if word not in firstMap:
            firstMap[word] = tempMap[word]
        else:
            for doc in tempMap[word]:
                firstMap[word][doc] = tempMap[word][doc]


if __name__ == "__main__":
    # PROGRAM RAN
    file_list = ["index1.json", "index2.json", "index3.json"]
    # COMBINE FILE_LIST
    mergeFiles(file_list)
    print("done")


from msilib.schema import Directory
from InvertedIndex import InvertedIndex

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


def main():
    query = input("ENTER QUERY: ")
    print(f"QUERY {query}")
    query_list = query.split()
    if len(query_list) == 1:
        # single query
        pass
    elif len(query_list) >= 2:
        # AND querying
        final_list = []
        for words_to_query in query_list:
            pass
    else:
        print("Exception")

if __name__ == "__main__":
    main()
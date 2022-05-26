import json

def ifWord(word):
    wB = False
    if word.strip().strip(':').startswith('"'):
        wB = True
    return wB


def end(word):
    return word.strip().startswith('}')


def test(file):
    aux = dict()
    temp = file.readline()
    counter = len(temp) + 1
    while file:
        temp = file.readline()
        if ifWord(temp[:-4]):
            aux[temp[:-4].strip().strip(':').strip('"')] = counter
        counter += len(temp) + 1
        if end(temp):
            break
        while True:
            temp = file.readline()
            counter += len(temp) + 1
            if end(temp):
                break
    return aux

def jumpPos(file, d, word):
    file.seek(0, 0)
    try:
        file.seek(d[word])
        file.readline()
        dStr = "{"
        for lines in file:
            if lines.strip().startswith('}'):
                dStr += lines.strip().strip(',')
                break
            else:
                dStr += lines
        return json.loads(dStr)
    except KeyError as err:
        print(f"Error, key: {err} invalid.")
    return {}

if __name__ == "__main__":
    f = open("test.json")
    print(test(f))
    jumpPos(f)
    f.close()

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
    counter = len(temp)
    print("Counter", counter)
    while file:
        temp = file.readline()
        counter += len(temp)
        print(counter, temp)
        if end(temp):
            break
        if ifWord(temp):
            aux[temp.strip().strip(':').strip('"')] = counter
        while True:
            temp = file.readline()
            counter += len(temp)
            if end(temp):
                break
    return aux

def jumpPos(file):
    file.seek(0, 0)
    file.seek(19)
    print(file.readline())
    return

if __name__ == "__main__":
    f = open("test.json")
    print(test(f))
    jumpPos(f)
    f.close()
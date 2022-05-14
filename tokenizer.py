import nltk

#tokenizes and stems content
def tokenizeContent(content):
    stemmer = nltk.stem.snowball.EnglishStemmer()
    tokens = []
    matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"
    content_list = content.split('\n')
    for line in content_list:
        finStr = ""
        i = 0
        for chars in line:
            if not(chars in matchString):
                chars = ' '
                if finStr and i and finStr[i-1] == ' ':
                    chars = ''
                    i -= 1
            finStr += chars
            i += 1
        if finStr:
            for strings in [s.lower() for s in finStr.split() if s.isalnum()]:     #lowercase strings in split
                #if strings not in STOPWORDS:
                tokens.append(stemmer.stem(strings))
    return tokens

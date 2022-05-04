
import nltk
import nltk.stem
from bs4 import BeautifulSoup, SoupStrainer
from nltk.stem import WordNetLemmatizer, PorterStemmer


def main():
    string = "housing"
    strings = ['artificial', 'intelligence', 'uci', 'shaping', 'the', 'future', 'of', 'ai', 'follow', 'us', 'toggle', 'navigation', 'home', 'about', 'us', 'events', 'team', 'contact', 'we', 're', 'ai', 'uci', 'artificial', 'intelligence', 'at', 'the', 'university', 'of', 'california', 'irvine', 'ai', 'uci', 'is', 'a', 'nonprofit', 'student', 'run', 'organization', 'that', 'focuses', 'on', 'promoting', 'and', 'cultivating', 'the', 'discipline', 'of', 'artificial', 'intelligence', 'and', 'machine', 'learning', 'and', 'its', 'applications', 'among', 'the', 'uci', 'community', 'bi', 'weekly', 'events', 'we', 'hold', 'workshops', 'meetings', 'for', 'the', 'curious', 'ones', 'to', 'learn', 'the', 'latest', 'technology', 'espcially', 'ai', 'connection', 'from', 'professionals', 'of', 'the', 'academia', 'to', 'almuni', 'from', 'the', 'industry', 'world', 'we', 'got', 'you', 'guys', 'connected', 'through', 'our', 'unique', 'seminars', 'meeting', 'time', 'pscb', '120', '6pm', '7pm', 'monday', 'only', 'some', 'of', 'our', 'past', 'workshops', 'for', 'those', 'who', 'couldn', 't', 'attend', 'our', 'meeting', 'due', 'to', 'space', 'constraints', 'don', 't', 'worry', 'we', 'have', 'you', 'covered', 'catch', 'up', 'with', 'our', 'youtube', 'video', 'linked', 'below', 'presentations', 'our', 'events', 'all', 'workshop', 'seminar', 'meeting', 'generating', 'fake', 'dating', 'profiles', 'with', 'stylegan', 'spam', 'classification', 'ics', 'day', 'style', 'transferring', 'natural', 'language', 'processing', 'hack', 'the', 'hackathon', 'computer', 'vision', 'and', 'opencv', 'workshop', 'machine', 'learning', '3', 'workshop', 'machine', 'learning', '2', 'workshop', 'machine', 'learning', '1', 'workshop', 'machine', 'learning', 'q', 'a', 'session', 'data', 'analytics', 'patterns', 'of', 'pallet', 'town', 'pt', '1', 'alexander', 'ihler', 'professor', 'ihler', 'is', 'the', 'advisor', 'of', 'ai', 'uci', 'here', 'are', 'some', 'areas', 'that', 'he', 'has', 'been', 'working', 'on', 'i', 'work', 'in', 'artificial', 'intelligence', 'and', 'machine', 'learning', 'focusing', 'on', 'statistical', 'methods', 'for', 'learning', 'from', 'data', 'and', 'on', 'approximate', 'inference', 'techniques', 'for', 'graphical', 'models', 'applications', 'of', 'my', 'work', 'include', 'data', 'mining', 'and', 'information', 'fusion', 'in', 'sensor', 'networks', 'computer', 'vision', 'and', 'image', 'processing', 'and', 'computational', 'biology', 'our', 'team', 'amy', 'elsayed', 'president', 'jason', 'kahn', 'vice', 'president', 'pooja', 'kumar', 'secretary', 'uddeshya', 'kumar', 'treasurer', 'madhumitha', 'govindaraju', 'corporate', 'chair', 'shivan', 'vipani', 'project', 'chair', 'michael', 'wang', 'web', 'master', 'citizen', 'of', 'the', 'world', 'and', 'a', 'web', 'developer', 'i', 'maintain', 'and', 'update', 'the', 'content', 'of', 'the', 'website', 'over', 'the', 'year', 'kash', 'iz', 'marketing', 'chair', 'omkar', 'pathak', 'lead', 'mentor', 'mathew', 'guerrero', 'historian', 'my', 'hero', 'is', 'elliot', 'alderson', 'and', 'i', 'like', 'house', 'of', 'leaves', 'alexander', 'zhang', 'mentor', 'andrew', 'laird', 'mentor', 'anthony', 'luu', 'mentor', 'brett', 'galkowski', 'mentor', 'eduardo', 'corona', 'mentor', 'monish', 'ramadoss', 'mentor', 'satyam', 'tandon', 'mentor', 'get', 'in', 'touch', 'meeting', 'infomation', 'pscb', '120', 'monday', 'only', '6', '7pm', 'email', 'aiatuci', 'gmail', 'com', 'thank', 'you', 'the', 'mailman', 'is', 'on', 'his', 'way', 'sorry', 'don', 't', 'know', 'what', 'happened', 'try', 'later', 'design', 'and', 'developed', 'by', 'michael', 'wang', 'and', 'themefisher', 'com', 'copyright', 'artificial', 'intelligence', 'uci', 'all', 'rights', 'reserved']
    # stemmer = nltk.stem.snowball.EnglishStemmer()
    # result = stemmer.stem(string)
    
    result = ""
    results = []
    try:
        wnl = nltk.WordNetLemmatizer()
    except LookupError:
        nltk.download('wordnet')
        wnl = nltk.WordNetLemmatizer()
    
    for word in strings:
        results.append(wnl.lemmatize(word))
    
    print(results)
    
    

if __name__ == "__main__":
    main()
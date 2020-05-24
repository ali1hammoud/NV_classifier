import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clear_data(text_procssing):
    #apply nltk tokenization
    tokens = nltk.word_tokenize(text_procssing)
    #delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation)]
    for i in range(0, len(tokens)):
        #The ‘sub’ in the function stands for SubString,
        #a certain regular expression pattern is searched in the given string(3rd parameter),
        #and upon finding the substring pattern is replaced by(2nd parameter).
        tokens[i] = re.sub('[^a-zA-Z]', '', tokens[i])
    #apply nltk lemmatization
    lemmatizer = WordNetLemmatizer() 
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    #delete stop_words
    stop_words = stopwords.words('english')
    stop_words.extend(['encyclopedia', 'wikipedia', 'free', 'wa', 'parser', 'jump', 'navigation', 'jump', 'search'])
    tokens = [i for i in tokens if ( i not in stop_words )]
    text_ready = ' '.join(tokens)
    return text_ready

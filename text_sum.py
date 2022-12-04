import spacy
from spacy.lang.ru.examples import sentences 

def getResult(f_s, s_s):
    nlp = spacy.load("ru_core_news_lg")
    f_s = nlp(f_s)
    s_s = nlp(s_s)

    return f_s.similarity(s_s)







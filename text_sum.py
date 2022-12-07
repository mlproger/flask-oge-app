import spacy
from api import make_celery

celery = make_celery()

@celery.task(name='web.getAnswer')
def getResult(f_s, s_s):
    nlp = spacy.load("ru_core_news_lg")
    f_s = nlp(f_s)
    s_s = nlp(s_s)
    return f_s.similarity(s_s)
    


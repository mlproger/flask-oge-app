import asyncio
import spacy
import difflib
from sentence_transformers import SentenceTransformer, util
import numpy as np


def getResult(f_s, s_s):
    print(1)
    nlp = spacy.load("ru_core_news_lg")
    print(2)
    f_s = nlp(f_s)
    s_s = nlp(s_s)
    return f_s.similarity(s_s)
    






# model = SentenceTransformer('symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli')
#     embedding1 = model.encode(f_s, convert_to_tensor=True)
#     embedding2 = model.encode(s_s, convert_to_tensor=True)
#     cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
#     print(float(cosine_scores))
#     return float(cosine_scores)
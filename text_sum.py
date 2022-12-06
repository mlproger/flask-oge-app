from sentence_transformers import SentenceTransformer, util


def getResult(f_s, s_s):
    model = SentenceTransformer('symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli')
    embedding1 = model.encode(f_s, convert_to_tensor=True)
    embedding2 = model.encode(s_s, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
    print(float(cosine_scores))
    return float(cosine_scores)






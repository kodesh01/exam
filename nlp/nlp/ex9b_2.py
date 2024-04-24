from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def bert_sim(text1,text2):
    model = SentenceTransformer('roberta-base-nli-mean-tokens')
    emb1 = model.encode(text1)[0]
    emb2 = model.encode(text2)[0]
    sim = cosine_similarity(emb1.reshape(-1,1),emb2.reshape(-1,1))
    return sim[0][0]
text1 = "I am Jerald"
text2 = "I am from MDU"
sim = bert_sim(text1,text2)
print('BERT Similarity : ',sim)

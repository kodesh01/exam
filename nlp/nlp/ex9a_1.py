import re
from collections import Counter
import math
import nltk

def cosine(text1,text2):
    def tokenize(text):
        words = re.findall(r'\w+',text.lower())
        return Counter(words)
    vec1 = tokenize(text1)
    vec2 = tokenize(text2)

    intersection = set(vec1.keys())&set(vec2.keys())
    dot_product = sum(vec1[word]*vec2[word] for word in intersection)
    mag1 = math.sqrt(sum(vec1[word]**2 for word in vec1.keys()))
    mag2 = math.sqrt(sum(vec2[word]**2 for word in vec2.keys()))
    cos_similarity=dot_product/(mag1*mag2)
    return cos_similarity

text1 = "I am Gopal"
text2 = "Everyone calls me Gopal"
sim = cosine(text1,text2)
print('Cosine Similarity : ',sim)

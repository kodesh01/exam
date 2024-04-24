import re
from collections import Counter
import math
import nltk

def jacard(text1,text2):
    def tokenize(text):
        words = re.findall(r'\w+',text.lower())
        return set(words)
    set1 = tokenize(text1)
    set2 = tokenize(text2)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    jacard = intersection/union
    return jacard

text1 = "I am Gopal"
text2 = "Everyone calls me Gopal"
sim = jacard(text1,text2)
print('Jaccard Similarity : ',sim)

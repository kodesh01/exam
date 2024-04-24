#Word n grams
import nltk
from nltk.util import ngrams
sentences=['Hi there','How are u','i am fine']
n=2
for senetence in sentences:
    words = senetence.split()
    word_ngrams = ngrams(words,n)
    for gram in word_ngrams:
        print(gram)
#Character ngrams:
import nltk
from nltk.util import ngrams
sentences=['Hi there']
n=2
for senetence in sentences:
    char_ngrams = ngrams(senetence,n)
    for gram in char_ngrams:
        print(gram)
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
sentence = input('Enter a senetence : ')
words = word_tokenize(sentence)
for word in words:
    stem_word = stemmer.stem(word)
    print(stem_word)
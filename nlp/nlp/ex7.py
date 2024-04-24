import nltk
from nltk.tokenize import word_tokenize
nltk.download('average_perceptron_tagger')
def pos(text):
    words = word_tokenize(text)
    tags = nltk.pos_tag(words)
    return tags
example = "The quick brown fox jumps over the lazy dog"
pos_tags=pos(example)
for word,tag in pos_tags:
    print(f"{word}:{tag}")
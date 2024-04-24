from nltk import word_tokenize
sentence = ['Hi there','How are u']
for text in sentence:
    print('Given sentence : ',text)
    tokens = word_tokenize(text)
    for token in tokens:
        print(f'** {token}')
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
data = "Hello everyone. I am under the water. Please help me."
stop = set(stopwords.words('english'))
words = word_tokenize(data)
words_filtered=[]
stop_list=[]
for word in words:
    if word not in stop:
        words_filtered.append(word)
    else:
        stop_list.append(word)
print(words_filtered)
print(stop_list)
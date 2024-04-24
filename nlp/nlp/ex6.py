from collections import defaultdict
def calculate_ngram_probabilities(corpus):
    ngrams =  defaultdict(int)
    context = defaultdict(int)
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words) - 2):
            trigram = tuple(words[i:i+3])
            ngrams[trigram] += 1
            context[trigram[:2]] += 1
    probabilities = defaultdict(float)
    for trigram, count in ngrams.items():
        context_count = context[trigram[:2]]
        probabilities[trigram] = (count + 1)/(context_count + len(ngrams))
    return probabilities
# Sample corpus
corpus = [
"I like to learn NLP",
"Coding is fun",
"Programming is interesting"
]
# Calculate trigram probabiities
trigram_probabilities = calculate_ngram_probabilities(corpus)
# Print trigram probabilities
for trigram, probability in trigram_probabilities.items():
    print(f"Trigram: {trigram}, Probability: {probability:.4f}")
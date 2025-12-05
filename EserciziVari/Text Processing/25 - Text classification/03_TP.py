import nltk
from nltk.corpus import movie_reviews
fields = movie_reviews.fileids()

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(10))

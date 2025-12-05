from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize
fields = movie_reviews.fileids()

sample = movie_reviews.raw("pos/cv944_13521.txt")

token = sent_tokenize(sample)
for lines in range(4):
    print(token[lines])

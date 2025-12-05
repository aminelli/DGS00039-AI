# Lets See how the movies are classified
import nltk
""" nltk.download('movie_reviews')#da eseguire solo la prima volta per recuperare la risorsa movie_reviews """ 

from nltk.corpus import movie_reviews

all_cats = []
for w in movie_reviews.categories():
    all_cats.append(w.lower())
print(all_cats)

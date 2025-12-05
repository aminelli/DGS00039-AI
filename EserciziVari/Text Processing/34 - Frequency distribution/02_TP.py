import nltk
""" nltk.download('brown') #da eseguire solo una volta per recuperare la risorsa brown """
#from nltk.tokenize import word_tokenize
from nltk.corpus import brown



cfd = nltk.ConditionalFreqDist(
          (genre, word)
          for genre in brown.categories()
          for word in brown.words(categories=genre))
categories = ['hobbies', 'romance','humor']
searchwords = [ 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=categories, samples=searchwords)

import nltk
from nltk.corpus import gutenberg

""" nltk.download('gutenberg') #da eseguire solo la prima volta per recuperare la risorsa gutenberg"""

fields = gutenberg.fileids()

print(fields)

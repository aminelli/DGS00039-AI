import nltk
from nltk.corpus import wordnet

""" nltk.download('wordnet') #da utilizzare solo alla prima esecuzione per scaricare la risorsa stopwords """

synonyms = []

for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print (set(synonyms))

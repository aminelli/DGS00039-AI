import nltk
""" nltk.download('conll2000')#da eseguire solo la prima volta per recuperare la risorsa conll2000 """

from nltk.corpus import conll2000

x = (conll2000.sents())
for i in range(3):
     print (x[i])
     print ('\n')

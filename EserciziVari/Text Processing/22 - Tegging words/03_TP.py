import nltk

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
sample = gutenberg.raw("blake-poems.txt")
tokenized = sent_tokenize(sample)
for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

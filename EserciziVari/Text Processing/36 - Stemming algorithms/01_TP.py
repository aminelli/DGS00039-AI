import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

porter_stemmer = PorterStemmer()
lanca_stemmer = LancasterStemmer()
sb_stemmer = SnowballStemmer("english",)

word_data = "Aging head of famous crime family decides to transfer his position to one of his subalterns"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)

print('***PorterStemmer****\n')
for w_port in nltk_tokens:
    print("Actual: %s  || Stem: %s" % (w_port, porter_stemmer.stem(w_port)))

print('\n***LancasterStemmer****\n')
for w_lanca in nltk_tokens:
    print("Actual: %s  || Stem: %s" % (w_lanca, lanca_stemmer.stem(w_lanca)))
print('\n***SnowballStemmer****\n')

for w_snow in nltk_tokens:
    print("Actual: %s  || Stem: %s" % (w_snow, sb_stemmer.stem(w_snow)))

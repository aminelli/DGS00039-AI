from nltk.corpus import wordnet as wn
# get all the antonyms
res_a = wn.lemma('horizontal.a.01.horizontal').antonyms()
print (res_a)

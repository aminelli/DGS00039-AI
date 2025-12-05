import nltk
""" nltk.download('averaged_perceptron_tagger') #da eseguire solo la prima volta per recuperare la risorsa averaged_perceptron_tagger """
text = nltk.word_tokenize("A Python is a serpent which eats eggs from the nest")
tagged_text=nltk.pos_tag(text)
print(tagged_text)

import nltk

sentence = [("The", "DT"), ("small", "JJ"), ("red", "JJ"),("flower", "NN"),
 ("flew", "VBD"), ("through", "IN"),  ("the", "DT"), ("window", "NN")]

grammar = "NP: {%s}" 

chunkprofile = nltk.RegexpParser(grammar)
result = chunkprofile.parse(sentence) 
print(result)
#result.draw()
import nltk

sentence = [("The", "DT"), ("small", "JJ"), ("red", "JJ"),("flower", "NN"), 
("flew", "VBD"), ("through", "IN"),  ("the", "DT"), ("window", "NN")]

grammar = "NP: {%s}" 

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence) 
print(result)
#result.draw()

import nltk
""" nltk.download('punkt') #da usare solo la prima volta per scaricare la risorsa """

FileName = ("Python\\Text Processing\\asset\\GodFather.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))

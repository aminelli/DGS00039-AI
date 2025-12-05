import nltk
from file_read_backwards import FileReadBackwards

with FileReadBackwards("Python\\Text Processing\\asset\\GodFather2.txt", encoding="utf-8") as BigFile:

# getting lines by lines starting from the last line up
# And tokenizing with applying reverse()
    for line in BigFile:
        word_data= line
        nltk_tokens = nltk.word_tokenize(word_data)
        nltk_tokens.reverse()
        print (nltk_tokens)

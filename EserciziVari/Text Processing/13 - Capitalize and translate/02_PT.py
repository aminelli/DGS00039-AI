import string

text = 'Tutorialspoint - simple easy learning.'

transtable = text.maketrans('tpol', 'wxyz')
print (text.translate(transtable))

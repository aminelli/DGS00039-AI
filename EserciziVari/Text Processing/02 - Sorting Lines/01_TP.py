
text_file = open("Python\\Text Processing\\asset\\poem.txt", "r")
data = text_file.readlines()
for i in range(len(data)):
   print (data[i])

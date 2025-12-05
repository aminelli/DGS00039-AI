text_file = open("Python\\Text Processing\\asset\\poem.txt", "r")
data = text_file.readlines()
data.sort()
for i in range(len(data)):
   print (data[i])

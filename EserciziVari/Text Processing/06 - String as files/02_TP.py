with open("Python\\Text Processing\\asset\\GodFather2.txt", "r") as BigFile:
    data=BigFile.read().replace('\n', '')
	
# Verify the string type 
print (type(data))
	
# Print the file content
print (data)

FileName = ("Python\\Text Processing\\asset\\GodFather.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print ( "Number of Words: ", len(lines_in_file.split()))

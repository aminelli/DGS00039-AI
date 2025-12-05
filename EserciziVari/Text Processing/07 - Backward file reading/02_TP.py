from file_read_backwards import FileReadBackwards

with FileReadBackwards("Python\\Text Processing\\asset\\GodFather2.txt", encoding="utf-8") as BigFile:

# getting lines by lines starting from the last line up
    for line in BigFile:
        print (line)

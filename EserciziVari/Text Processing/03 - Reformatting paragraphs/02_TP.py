import textwrap3

FileName = open("Python\\Text Processing\\asset\\poem2.txt", "r")

print("**Before Formatting**")
print(" ")

data = FileName.readlines()
for i in range(len(data)):
    print(data[i])

print(" ")
print("**After Formatting**")
print(" ")

FileName = open("Python\\Text Processing\\asset\\poem2.txt", "r")
data = FileName.readlines()
for i in range(len(data)):
    dedented_text = textwrap3.dedent(data[i]).strip()
    print(dedented_text)

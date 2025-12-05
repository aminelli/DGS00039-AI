# Can not reassign
t = "Tutorialspoint"
print(type(t))
""" t[0] = "M" """

x = 'banana'

for idx in range(0, 5):
    print(x[idx], "=", id(x[idx]))

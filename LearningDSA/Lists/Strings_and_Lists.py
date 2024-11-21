# creating lists to strings

a = "spam"
b = list(a)
print(b[2])

a ="spam spam spam"
b = a.split()
print(b)

a ="spam-spam-spam"
b = a.split("-")    # passing delimiter as parameter
print(b)

a ="spam-spam-spam"
b = a.split("a")    # passing delimiter as parameter
print(b)
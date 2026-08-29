a={10,20,"apple",4.2}
print(a) 

a.add(1)
print(a)

a.remove("apple")
print(a)

# a.remove(12312)
# print(a)          it gives error because 12312 is not in set

a.discard(12312)
print(a)             #it not gives error

a.pop()
print(a)
text="Hello world"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

name="  Shweta  "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

text="Python is fun"
print(text.find("fun"))
print(text.replace("fun","aewsome"))

fruits="apple,banana,orange"
print(fruits.split(","))
print(",".join(['apple', 'banana', 'orange']))

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())

text="Hello, World!"
print(len(text))

print(ord("A"))
print(chr(65))
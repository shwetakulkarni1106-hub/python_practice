text=input("enter string: ")
count=0
for ch in text:
    if ch in"aeiouAEIOU":
        count+=1
print("number of vowel's: ", count)
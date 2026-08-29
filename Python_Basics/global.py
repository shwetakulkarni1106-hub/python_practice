def sum(a,b):
    global z
    z=8    #refer as lobal variable not local
    return a+b


z=6
print(sum(2,3))
print(z)
def hi (x,y,v):
    value =((x > y) or (y>x) or (y>v) or (x>v))
    return value
a=3
b=7
v=6
print(hi(a,b,v))
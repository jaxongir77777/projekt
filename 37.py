def sign(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    else :
        return 1
a=input()
b=input ()
s=sign(float(a))+sign(float(b))
print (s)

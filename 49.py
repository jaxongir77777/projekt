n=input('n=')
n=int(n)
s=0
from math import*
for i in range(1,n+1):
 p=1
 for j in range(1,n+1):
    p*=(sin(j)+i**2)
 s+=p
print('s=',s)
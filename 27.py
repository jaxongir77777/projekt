a=[15,78,45,8,42]

for i in range (len(a)):
    m=i
    for j in range ( i ,len(a)):
        if a[m]>a[j]:
         m=j
        x=a[i]    
    a[i]=a[m]
    a[m]=x
print(a)

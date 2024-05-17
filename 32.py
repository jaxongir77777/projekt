
a=input(" ko'd kiriting ")
b=("jaxongir")
d=("begzod")
c=5555
if a==b:
    print ("xush kelibsiz")
    yosh = input("Yoshingizni kiriting: ")
    try:
        yosh = int(yosh) 
    except:
        print("Butun son kiritmadingiz")
    else:
        print(f"Siz {2024-yosh} yilda tug'ilgansiz")
elif a==d:
    print ("xush kelibsiz")
    yosh = input("Yoshingizni kiriting: ")
    try:
        yosh = int(yosh) 
    except:
        print("Butun son kiritmadingiz")
    else:
        print(f"Siz {2024-yosh} yilda tug'ilgansiz")
elif a==c:
    print ("xush kelibsiz")
else:
    print ("siz noto'g'ri ko'd kiritdingiz")
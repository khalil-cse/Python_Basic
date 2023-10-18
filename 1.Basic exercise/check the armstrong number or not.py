n=int(input("Enter three digit:")) #371
a=n%10 #1
num=n//10
b=num%10 #7
c=num//10 #1
if (a**3)+(b**3)+(c**3)==n:   #3**3+7**3+1**3=371
    print("The number is armstrong")
else:
    print("Not armstrong")
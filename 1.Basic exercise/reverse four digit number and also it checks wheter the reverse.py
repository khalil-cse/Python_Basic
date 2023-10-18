x=int(input("Enter the four digit number:"))
a=x%10 #to get last number
num1=x//10 #to get first three numbers
b=num1%10
num2=num1//10
c=num2%10
d=num2//10
rev=a*1000+b*100+c*10+d # formula for reverse
print(rev)
if x==rev:
    print(True)
else:
    print(False)

#if value 4561 so a=1,num1=456,b=6,num2=45,c=5,d=4
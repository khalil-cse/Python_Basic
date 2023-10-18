#9474 is a 4-digit narcissistic number because:
#9^4 + 4^4 + 7^4 + 4^4 = 9474

x=int(input("Enter the four digit number:"))
a=x%10 #to get last number
num1=x//10 #to get first three numbers
b=num1%10
num2=num1//10
c=num2%10
d=num2//10
if (a**4)+(b**4)+(c**4)+(d**4)==x:   #3**3+7**3+1**3=371
    print("The number is narcissitic")
else:
    print("Not narcissitic")
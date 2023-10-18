n=int(input("Enter the three digit number:"))  # for example input 246
a=n%10  #6
num=n//10
b=num%10 #4
c=num//10 #2
result=(a*a)+(b*b)+(c*c) # or result=(a**2)+(b**2)+(c**2) is same result
print(result)
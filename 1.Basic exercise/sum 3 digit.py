x=int(input("Enter the three digit number:"))
a=x%10  # if value 541 then,a=1 num=54,b=4,c=5
num=x//10
b=num%10
c=num//10
sum=a+b+c
print(sum)

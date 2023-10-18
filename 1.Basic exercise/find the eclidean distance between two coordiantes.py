import math
x1=float(input("X1:"))
y1=float(input("y1:"))
x2=float(input("X2:"))
y2=float(input("y2:"))
x=[x1,y1]
y=[x2,y2]

distance=round(math.dist(x,y),2)
print("Distance:",distance)
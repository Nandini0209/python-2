#Write a Python program to calculate surface volume and area of a cylinder

import math

r=float(input("enter the radius:"))
h=float(input("enter the height:"))

area = 2*math.pi*r*(r+h)
volume= math.pi*r**2*h

print("the area of the cylinder is:",area)
print("the volume of the cylinder is :",volume)

#Write a Python program to calculate the area of regular polygon.
import math
ns = int(input("Enter the number of sides: "))
ls = int(input("Enter the lenght of sides: "))
apothem = ls / (2 * math.tan(math.pi/ns))
perimeter = ns * ls
area = (perimeter * apothem)/2
print("The area of regular polygon :", int(area))
"""
Write python program to find :

(a) Area and perimeter of a triangle when all three sides are given.
Hint: (Use Heron’s Equation)

(b) Find all three angles of the triangle given in (a)

Display the input data and results in proper format.

"""

#Solution

a=int (input("enter the vlaue of side a:"))
b=int (input("enter the vlaue of side b:"))
c=int (input("enter the vlaue of side c:"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
perimeter=2*s
print("area of triangle is:",area)
print("perimeter of triangle is:",perimeter)

import math
angle_a=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
print("The value of angle a is :",angle_a)
angle_b=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
print("The value of angle b is :",angle_b)
angle_c=math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
print("The value of angle c is :",angle_c)


print("angle A, B, C",angle_a,angle_b,angle_c)


                                    





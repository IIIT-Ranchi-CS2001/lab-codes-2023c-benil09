"""
Write a program to find the roots of a quadratic equation when the
coefficients a, b and c are given ( assume that a, b and c are integers)
 Hint: find the discriminant d= b2 − 4ac
 
If d = 0, the equation has one real repeated root (both roots are the same:
    R1= R2 = -b/(2a)
    
If d > 0, the equation has two distinct real roots.
    R1= (-b + sqrt(d))/2a
    R2= (-b - sqrt(d))/2a
If d < 0, the equation has two complex roots.
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)

"""
import math

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

D=(b**2)-4*a*c
print("The value of D is : ",D)
if D==0:
    print("The equation has one real repeated root")
    print("R1 = R2 = ",-b/(2*a))
elif D>0:
    print("The equation has two distinct real roots  ")
    print("The value of R1 is :",(-b+math.sqrt(D)/(2*a)))
    print("The value of R2 is :",(-b-math.sqrt(D)/(2*a)))
else:
    print("The equation has two comples roots")
    print("The two complex roots are:",complex(-b/(2*a),math.sqrt(-D)/(2*a)))
    print("The two complex roots are:",complex(-b/(2*a),-math.sqrt(-D)/(2*a)))
    
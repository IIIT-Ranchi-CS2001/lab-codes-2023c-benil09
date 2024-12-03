"""
Write a program to find:

a. The equivalent impedance when two impedances Z1 and Z2
are connected in parallel.

b. Display Z1 and Z2 in complex form.

c. Display the real part and imaginary part of the result in separate
lines.

"""

#solution (a)
Z1_real= float(input("Enter the real part of Z1: "))
Z1_imag= float(input("Enter the imag part of Z1: "))
Z2_real= float(input("Enter the real part of Z2: "))
Z2_imag= float(input("Enter the imag part of Z2: "))

Z_eq=(complex(Z1_real,Z1_imag)*complex(Z2_real,Z2_imag))/(complex(Z1_real,Z1_imag)+complex(Z2_real,Z2_imag))
print("The equivalent resistance of Z1 and Z2 in parallel are : ",Z_eq)

#solution (b)

Z1=complex(Z1_real,Z1_imag)
print("Z1 in comples form can be written as :",Z1)

Z2= complex(Z2_real,Z2_imag)
print("Z2 in comples form can be written as :",Z2)


#solution (c)
print ("The real part of the Z_eq is:", Z_eq.real)
print ("The imag part of the Z_eq is:", Z_eq.imag)




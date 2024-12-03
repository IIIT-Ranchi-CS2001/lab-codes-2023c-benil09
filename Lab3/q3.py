"""
Write a python script to print the first n terms of the Fibonacci series using while loop
"""


n = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a, b = 0, 1
count = 0

print("Fibonacci Series:")

# Use a while loop to print the Fibonacci series up to n terms
while count < n:
    print(a, end=" ")
    # Update values for the next iteration
    a, b = b, a + b
    count += 1
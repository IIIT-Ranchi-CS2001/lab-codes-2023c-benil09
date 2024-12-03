"""
Write a python script to find the squares of first n natural numbers. Display
both the number and the square as shown below. Use while loop

        Number          Square
        1               1
        2               4
        3               9
        4               16
        .               .
        .               .
        n               n^2
"""

n=int (input("Enter the value of n:"))

i=1
print( "Number        Square")
while(i <=n):
   
    print(f" {i}               {i**2}")
    i=i+1
    
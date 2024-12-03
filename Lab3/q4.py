"""
Write a python script to print the multiplication table of a given number up
to the specified limit using a for loop.

"""

n=int (input("Enter the limit : "))
num=int(input("Enter the number : "))
for i in range(1,n+1):
    print(num,"*",i,"=",num*i)  # print the multiplication table of num up
    

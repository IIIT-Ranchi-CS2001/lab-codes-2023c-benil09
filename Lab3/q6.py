"""
Write a python script to find the number of occurrences of a particular
character present in the given string using a loop. (Don’t use string
methods).
"""

str=input("Enter the string:")
char=input("Enter the character:")
count=0
for i in str :
    if i == char :
        count = count + 1
        
print(f"the characer '{char}' occurs '{count}' times  ")
    
        
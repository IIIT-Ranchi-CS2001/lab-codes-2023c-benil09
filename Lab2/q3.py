"""
3. Write a python script to enter any string at run time and check whether it is a palindrome or not.

"""

S="madamn"
S1=S[::-1]

if(S!=S1):
    print("The string is not a palindrome")
else:
    print("The String is palindrome")
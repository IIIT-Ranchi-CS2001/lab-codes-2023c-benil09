"""
Write a python script to find the sum of the digits of the given number using
a while loop. Display the number and the sum.

"""

num=int(input("Enter the value of num : "))

sum=0
while(num!=0):
    digit=num%10
    sum+=digit
    num=num/10
    print("The extracted digit is",digit)
    num=int(num)
    print("The number rem. is : ",num)
    print("Sum of the digits till now  is : ",sum)
    print("Final Sum of the digits is : ",sum)  # Removed the while loop here
    print("\n")
    

    

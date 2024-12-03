"""
Enter the following details of a student at run time: - Name, Roll
number and marks secured for Mathematics Examination out of 100.

Write a python script to display student details as shown:
    Name:
    Roll Number:
    Marks:
    Grade Point:
    Remark:
The criteria for awarding grade point and remark are as given in the
table:
"""

Name=input("Enter your name:")
Roll_Number=input("Enter your Roll Number:")
Marks=int(input("Enter the marks obtained in Mathematics:"))

if(Marks >=90):
    Grade_Point="10"
    Remark="OUTSTANDING"
elif(Marks >=80 and Marks < 90):
    Grade_Point="9"
    Remark="VERY GOOD"
elif(Marks >=70 and Marks < 80):
    Grade_Point="8"
    Remark="GOOD"
elif(Marks >=60 and Marks < 70):
    Grade_Point="7"
    Remark="AVERAGE"
elif(Marks >=50 and Marks<60):
    Grade_Point="6"
    Remark="PASS"
elif(Marks<50):
    Grade_Point="0"
    Remark="FAIL"
    
print("Name:",Name)
print("Roll Number:",Roll_Number)
print("Marks:",Marks)
print("Grade:",Grade_Point)
print("Remark:",Remark)
"""
Generate three lists using list comprehension. List of names, list of Roll nos
and list of marks for Physics exam for all students of the class. Create a list
of tuples using the zip function where each tuple carries individual student
details. Sort the list of tuples using a sorted function by keeping Marks as the
key for sorting.
"""


# Generate three lists using list comprehension
names = [f"Student_{i}" for i in range(1, 11)] 
roll_nos = [f"Roll_{i}" for i in range(1, 11)]  
marks = [87, 92, 75, 63, 81, 95, 78, 88, 70, 85] 

student_details = list(zip(names, roll_nos, marks))

sorted_students = sorted(student_details, key=lambda x: x[2], reverse=True)

print("Original List of Student Details:")
for student in student_details:
    print(student)

print("\nSorted List of Student Details by Marks:")
for student in sorted_students:
    print(student)
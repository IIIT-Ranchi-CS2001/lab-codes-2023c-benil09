"""
Generate 2 lists (course code and course name). create a new list with both
course code and name like["CS1001:Python"...]
"""



course_codes = ["CS1001", "MA1002", "PH1003", "CH1004"]
course_names = ["Python", "Calculus", "Physics", "Chemistry"]

combined_courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

# Output the result
print(combined_courses)
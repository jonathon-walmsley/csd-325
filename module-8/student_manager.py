# Jonathon Walmsley
# 07/12/2026
# Module 8.2
# Purpose: Demonstrate usage of Json

import json

def student_helper(records):
    for record in records:
        print(f"{record['L_Name']}, {record['F_Name']} : ID = {record['Student_ID']}, Email = {record['Email']}")

with open('Student.json', 'r') as f:
    students = json.load(f)

print('This is the original Student list.')
student_helper(students)

my_data = {'L_Name': 'Walmsley', 'F_Name': 'Jonathon', 'Student_ID': 12345, 'Email': 'jwalmsley@my365.bellevue.edu'}

students.append(my_data)

with open('Student.json', 'w') as f:
    json.dump(students, f, indent=4)

print('This is the updated Student list.')
student_helper(students)


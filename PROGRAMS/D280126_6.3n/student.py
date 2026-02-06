'''
write a python function that parses a nested dictionary of student information Requirements: 
Full Name
o Branch
o SGPA

example input:
"full_name": "Alice Johnson",
            "branch": "Computer Science",
            "sgpa": 8.5
        },
        "full_name": "Bob Smith",
            "branch": "Mechanical Engineering",
            "sgpa": 7.8
        }
'''
def parse_student_info(students):
    parsed_info = []
    for student_id, info in students.items():
        student_data = {
            "Full Name": info.get("full_name"),
            "Branch": info.get("branch"),
            "SGPA": info.get("sgpa")
        }
        parsed_info.append(student_data)
    return parsed_info
# Example usage
students = {
    "student_1": {
        "full_name": "Alice Johnson",
        "branch": "Computer Science",
        "sgpa": 8.5
    },
    "student_2": {
        "full_name": "Bob Smith",
        "branch": "Mechanical Engineering",
        "sgpa": 7.8
    },
    "student_3": {
        "full_name": "Charlie Brown",
        "branch": "Electrical Engineering",
        "sgpa": 9.1
        }
}
parsed_students = parse_student_info(students)
for student in parsed_students:
    print(student)

'''
{'Full Name': 'Alice Johnson', 'Branch': 'Computer Science', 'SGPA': 8.5}
{'Full Name': 'Bob Smith', 'Branch': 'Mechanical Engineering', 'SGPA': 7.8}
{'Full Name': 'Charlie Brown', 'Branch': 'Electrical Engineering', 'SGPA': 9.1}
'''
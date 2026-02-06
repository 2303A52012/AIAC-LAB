def student_report(student_data):# dist as input
    name = student_data['name']
    age = student_data['age']
    marks = student_data['marks']
    average_mark = sum(marks) / len(marks)
    ispass = isPass(average_mark)
    return {
        'name': name,
        'age': age,
        'average_mark': average_mark,
        'is_pass': ispass
        }

def isPass(average_mark):
    return average_mark >=40

# Example usage
if __name__ == "__main__":
    students=[
        {
        'name': 'Alice',
        'age': 20,
        'marks': [85, 90, 78]
    },
    {
        'name': 'Bob',
        'age': 22,
        'marks': [35, 40, 30]
    },
    {
        'name': 'Charlie',
        'age': 21,
        'marks': [60, 70, 65]
    }
    ]
    passlist=[]
    for student in students:
        report = student_report(student)
        if report['is_pass']:
            passlist.append(report['name'])
    print("pass list:", passlist)
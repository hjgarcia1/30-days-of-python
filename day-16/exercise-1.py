# def get_name(student):
#     return student["name"]

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

# students.sort(key=get_name)

students.sort(key=lambda student: student["name"])

print(students)

from os import name

student_mark = {
    "alice":90,
    "bob":76,
    "charlie":98,
    "david":89,
}
name = input("Enter the student's name: ")
if name in student_mark:
    print(f"{name}'s mark: {student_mark[name]}")
else:
    print("Student not found.")
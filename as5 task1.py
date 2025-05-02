marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 80,
    "David": 76
}

name = input("Enter the Student's name: ")

if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")
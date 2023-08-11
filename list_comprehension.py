# def main():
#     yell("This", "is", "cs50")


# def yell(*phrase):
#     uppercased = [str.upper() for str in phrase]
#     print(*uppercased)


# if __name__ == "__main__":
#     main()


students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ron", "house": "Gryffindor"},
]

students_in_gryffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
print(students_in_gryffindor)

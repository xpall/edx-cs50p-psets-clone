import csv

teachers = []


with open("teachers_names.csv") as teachers_name:
    for line in teachers_name:
        name, surname = line.rstrip().split(",")
        teacher = {"name":name, "surname":surname}
        teachers.append(teacher)


for teacher in sorted(teachers, key=lambda surname: len(surname['surname']), reverse=True):
    print(f"{teacher['name']}'s surname is {teacher['surname']}")
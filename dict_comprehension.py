students = ["Harry", "Hermione", "Ron"]


# dictionary comprehension
# gryffindors = [({"name": student}, {"house": "Gryffindor"}) for student in students]
# gryffindors = {student:"Gryffindor" for student in students}

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

for i, student in enumerate(students):
    print(i+1, student)


def main():
    student = get_student()
    if student["Name"] == "Padma":
        student["House"] = "Ravenclaw"
    print (f"{student['Name']} from {student['House']}")


def get_student():
    students = {}
    students["Name"] = input("Name: ")
    students["House"] = input("House: ")
    return students


if __name__ == "__main__":
    main()
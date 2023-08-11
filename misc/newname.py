import csv

firstname = input("What is your first name? ")
surname = input("What is your last name? ")

with open("teachers_names.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([firstname, surname])


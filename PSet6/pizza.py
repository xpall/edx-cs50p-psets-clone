import sys
import csv
from tabulate import tabulate


def main():
    convert_table(argv_check())


def argv_check():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


def convert_table(f):
    try:
        temp = []
        with open(f) as file:
            file = csv.reader(file)
            for row in file:
                temp.append(row)
        print(tabulate(temp, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__=="__main__":
    main()
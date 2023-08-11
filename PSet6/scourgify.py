import csv
import sys


def main():
    scourgify(argv_checker())


def argv_checker():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


def scourgify(f):
    try:
        with open(f, 'r') as old_format:
            csv_reader = csv.DictReader(old_format)
            with open(sys.argv[2], 'w') as new_format:
                csv_writer = csv.DictWriter(new_format, fieldnames=['first', 'last', 'house'])
                csv_writer.writeheader()
                for line in csv_reader:
                    last, first = line['name'].split(", ")
                    house = line['house']
                    csv_writer.writerow({
                        'first' : first,
                        'last' : last,
                        'house' : house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__=="__main__":
    main()
import sys


def main():
    count_code_lines(check_argv())


def check_argv():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        return str(sys.argv[1])


def count_code_lines(c):
    try:
        code_lines = 0
        code_tempstorage = []
        with open(c) as file:
            for line in file:
                code_tempstorage.append(line.lstrip())
            for line in code_tempstorage:
                if len(line) != 0 and not line.startswith(("#")):
                    code_lines += 1
        print(code_lines)
    except (FileNotFoundError):
        print("File does not exist")


if __name__=="__main__":
    main()
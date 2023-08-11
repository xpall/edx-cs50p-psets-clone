numbers = "0123456789"

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum() and s[:2].isalpha() and 2 <= len(s) <= 6:
        allnum = ""
        for char in s:
            if char in numbers:
                position = int(s.index(char))
                allnum = str(s[position::])
                break
        if allnum == "":
            return True
        elif allnum.isdigit() and allnum[0] !="0":
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
#first number is not 0; ??? get index of first number, check if >0, split from index, check remaining if there numbers only
alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
alpha_num = list(alphabet + numbers)

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0] in alphabet and s[1] in alphabet:
            for char in s:
                if char not in alpha_num:
                    s = False
                    return s
            for i, char in enumerate(s):
                if char.isdigit():
                    return i
                else:
                    None
            s = s.lstrip[i]
            for char in s:
                if char not in numbers:
                    s =  False
            return s

main()


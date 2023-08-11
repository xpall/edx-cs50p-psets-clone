import re

def main():
    email = input("Enter your email: ")
    email_checker(email)


def email_checker(prompt):
    if re.search(r".+@.+\.edu", prompt):
        print("Valid email")
    else:
        print("Invalid email")


if __name__=="__main__":
    main()
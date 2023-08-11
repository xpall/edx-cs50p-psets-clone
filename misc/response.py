import validators

def main():
    print(email_validator((input("What's your email address? "))))


def email_validator(str):
    if validators.email(str) == True:
        return 'Valid'
    else:
        return 'Invalid'


if __name__=="__main__":
    main()
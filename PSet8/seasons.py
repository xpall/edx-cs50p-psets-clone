import sys
import re
import inflect
from datetime import date


p = inflect.engine()


def main():
    finalize(convert_days_to_minutes(get_difference_in_days((get_valid_birthdate(input("Date of birth: "))))))


def get_valid_birthdate(birthdate):
    if birth_date := re.search(r"(\d{4})-(\d{2})-(\d{2})", birthdate):
        if int(birth_date.group(2)) <= 12 and int(birth_date.group(3)) <= 31:
            return birthdate
    else:
        sys.exit("Invalid date")


def get_difference_in_days(birthdate):
    present_date = str(date.today())
    yyyy, mm, dd = birthdate.split("-")
    yyyy2, mm2, dd2 = present_date.split("-")
    date1 = date(int(yyyy), int(mm), int(dd))
    date2 = date(int(yyyy2), int(mm2), int(dd2))
    delta = date2 - date1
    return str(delta)


def convert_days_to_minutes(days):
    days = int(re.sub(r' days, 0:00:00', '', days))
    minutes = days * 60 * 24
    words = p.number_to_words(minutes)
    return (f"{words} minutes")


def finalize(t):
    t = re.sub(r"and ", "", t)
    print(t.capitalize())


if __name__ == "__main__":
    main()
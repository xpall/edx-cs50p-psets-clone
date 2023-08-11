import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if twelve_hours := re.search(r'^(\d{1}\d?(?::\d{2})?) (AM|PM) to (\d{1}\d?(?::\d{2})?) (AM|PM)$', s):
            hour_1, hour_2 = pm_adjust(twelve_hours.group(1), twelve_hours.group(2)), pm_adjust(twelve_hours.group(3), twelve_hours.group(4))
            minute_1, minute_2 = minute_checker(twelve_hours.group(1)), minute_checker(twelve_hours.group(3))
            return f'{hour_1}:{minute_1} to {hour_2}:{minute_2}'
        else:
            raise ValueError
    except ValueError:
        return ValueError


def minute_checker(t):
    if ':' not in t:
        return '00'
    elif ':' in t:
        if int(t[-2::]) < 60:
            return t[-2::]
        else:
            raise ValueError
    else:
        return '00'


def pm_adjust(t, x):
    if 'PM' in x and ':' in t:
        h, _ = t.split(':')
        return (int(h) + 12)
    elif 'PM' in x:
        return int(t) + 12
    elif 'AM' in x and ':' in t:
        h, _ = t.split(':')
        return h
    elif 'AM' in x:
        return t


if __name__=="__main__":
    main()
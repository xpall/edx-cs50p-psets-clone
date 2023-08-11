import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if twelve_hours := re.search(r'^(\d{1}\d?(?::\d{2})?) (AM|PM) TO (\d{1}\d?(?::\d{2})?) (AM|PM)$', s):
            hour_1, hour_2 = pm_adjust(twelve_hours.group(1), twelve_hours.group(2)), pm_adjust(twelve_hours.group(3), twelve_hours.group(4))
            minute_1, minute_2 = minute_checker(twelve_hours.group(1)), minute_checker(twelve_hours.group(3))
            return f'{hour_1}:{minute_1} to {hour_2}:{minute_2}'
        else:
            raise ValueError
    except ValueError:
        return ValueError


def minute_checker(t):
    if len(t) >= 4 and int(t[-2::]) > 60:
        _, m = t.split(':')
        return m
    elif len(t) <= 3:
        return '00'
    else:
        pass


def pm_adjust(t, x):
    if 'PM' in x:
        if len(t) == 4 or len(t) == 5:
            h, _ = t.split(':')
            return (int(h) + 12)
        else:
            return (int(t) + 12)
    else:
        try:
            h, _ = t.split(':')
            return h
        except ValueError:
            return t


if __name__=="__main__":
    main()
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if schedule := re.search(r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$', s):
        time_in_h = convert_hours(valid_hours(schedule.group(1)), schedule.group(3))
        time_in_min = valid_minutes(schedule.group(2))
        #time_in_am_pm = schedule.group(3)
        time_out_h = convert_hours(valid_hours(schedule.group(4)), schedule.group(6))
        time_out_min = valid_minutes(schedule.group(5))
        #time_out_am_pm = schedule.group(6)
        #print(f'{time_in_h.zfill(2)}:{time_in_min} {time_in_am_pm} to {time_out_h.zfill(2)}:{time_out_min} {time_out_am_pm}')
        return f'{time_in_h.zfill(2)}:{time_in_min} to {time_out_h.zfill(2)}:{time_out_min}'
    else:
        raise ValueError


def valid_minutes(t):
    if t:
        if int(t) < 60:
            return t
        else:
            raise ValueError
    else:
        return '00'


def convert_hours(h, am_pm):
    if am_pm == 'PM':
        if h == '12':
            return '12'
        else:
            h = int(h) + 12
            return str(h)
    elif am_pm == 'AM':
        if h == '12':
            return '00'
        else:
            return str(h)


def valid_hours(t):
    if int(t) <= 12:
        return str(t)
    else:
        raise ValueError


if __name__=="__main__":
    main()
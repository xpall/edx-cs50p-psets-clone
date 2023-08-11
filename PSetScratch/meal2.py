def main():
    time = str(input("What time is it? ")).lower().replace(" ", ":")
    if "p.m." in time:
        time = format12pm(time)
    elif "a.m." in time:
        time = format12am(time)
    else:
        time = format24(time)

def eatingTime(x):
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")
    return(x)


def format24(x):
    x = x.split(":")
    h = float(x[0])
    m = float(x[1])
    x = round((h + (m / 60)), 2)
    eatingTime(x)

def format12pm(x):
    x = x.split(":")
    h = float(x[0])
    m = float(x[1])
    if h == 12:
        h = 0
        return
    x = round(((h + 12) + (m / 60)), 2)
    eatingTime(x)

def format12am(x):
    x = x.split(":")
    h = float(x[0])
    m = float(x[1])
    if h == 12:
        h = 0
        return()
    x = round((h + (m / 60)), 2)
    eatingTime(x)

if __name__ == "__main__":
    main()
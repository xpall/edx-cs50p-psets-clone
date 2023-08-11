def main():
    time = str(input("What time is it? "))
    hformat = convert(time)

def convert(x):
    x = x.split(":")
    h = float(x[0])
    m = float(x[1])
    x = round((h + (m / 60)), 2)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")
    return(x)

if __name__ == "__main__":
    main()
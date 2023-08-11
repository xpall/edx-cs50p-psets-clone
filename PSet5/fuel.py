def main():
    n = str(input("Fuel: "))
    result = gauge(convert(n))
    print(result)


def convert(n):
    while True:
        try:
            n = n.split("/")
            x = int(n[0])
            y = int(n[1])
            n = round((x / y) * 100)
            if y == 0:
                raise ZeroDivisionError
            elif x > y or x != x:
                raise ValueError

        except IndexError:
            continue
        else:
            return n


def gauge(number):
    if number <= 1:
        return ("E")
    elif number >= 99:
        return ("F")
    else:
        return (f"{number}%")


if __name__ == "__main__":
    main()
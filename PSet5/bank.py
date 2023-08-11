def main():
    greet = str(input("Greetings: ")).strip().replace(" ","")
    amount = value(greet)
    print(f"${amount}")


def firstWordTest(l):
    l = l[0:5]
    return(l)


def firstLetterTest(l):
    l = l[0]
    return(l)


def value(greet):
    if firstWordTest(str(greet)).lower() == "hello":
        return 0
    elif firstLetterTest(str(greet)).lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
def main():
    yell("This", "is", "cs50")


def yell(*phrase):
    # map(function, ite)
    uppercased = map(str.upper, phrase)
    print(*uppercased)


if __name__ == "__main__":
    main()
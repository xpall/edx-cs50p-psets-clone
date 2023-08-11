def main():
    string = str(input("Your text: "))
    print(shorten(string))


def shorten(word):
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            word = word.replace(char,"")
    return word


if __name__ == "__main__":
    main()
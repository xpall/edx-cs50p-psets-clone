import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    print(re.findall(pattern, s, re.IGNORECASE))
    um_occurences = len(re.findall(pattern, s, re.IGNORECASE))
    return um_occurences

if __name__ == "__main__":
    main()
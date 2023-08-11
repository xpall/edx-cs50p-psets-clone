import random
import sys

def main():
    game(level("Level: "))

def level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                continue
            else:
                n = random.randint(1, n)
                return n
        except ValueError:
            continue

def game(prompt):
    while True:
        try:
            answer = int(input("Guess: "))
            if answer > prompt:
                print("Too large!")
                continue
            elif answer < prompt:
                print("Too small!")
                continue
            else:
                sys.exit("Just right!")
        except ValueError:
            continue

main()
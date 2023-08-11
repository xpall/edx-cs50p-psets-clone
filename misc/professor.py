import random
import re


def get_level():
    while True:
        try:
            prompt = int(input("Level: "))
            if prompt in [1, 2, 3]:
                return int(prompt)
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


def main():
    incorrect = 0
    score = 0
    level = get_level()
    x, y = generate_integer(level)
    for _ in range(10):
        answer = x + y
        ans = input(f"{x} + {y} = ")
        if int(ans) == answer:
            score += 1
            incorrect = 0
            x, y = generate_integer(level)
        else:
            for _ in range(2):
                if int(ans) != answer:
                    print("EEE")
                    ans = input(f"{x} + {y} = ")
                    incorrect += 1
                else:
                    score += 1
                    incorrect = 0
                    x, y = generate_integer(level)
                    break
            if incorrect == 2:
                print("EEE")
                print(f'{x} + {y} = {answer}')
                incorrect = 0
                x, y = generate_integer(level)
    print(score)


if __name__ == "__main__":
    main()
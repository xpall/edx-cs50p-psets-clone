import random


def main():
    level = get_level()
    generate_integer(level)
    game(level)


def get_level():
    while True:
        try:
            prompt = int(input("Level: "))
            if prompt in [1, 2, 3]:
                return prompt
            raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return x,y


def game(level):
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        guess = str(input(f"{x} + {y} = "))
        if guess != str(x + y):
            x2, y2 = x, y
            incorrect = 1
            print("EEE")
            while incorrect != 3:
                guess2 = str(input(f"{x2} + {y2} = "))
                if guess2 == str(x2 + y2):
                    score +=1
                    break
                else:
                    print("EEE")
                    incorrect += 1
            else:
                print(f"{x2} + {y2} = {x2 + y2}")
        else:
            score += 1
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
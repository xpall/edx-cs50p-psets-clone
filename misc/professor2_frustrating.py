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
    # check50 does not like codes below
    # start_integers, end_integers = {1:0, 2:10, 3:100}, {1:9, 2:99, 3:999}
    # random_number = random.randint(start_integers[level], end_integers[level])
    # return random_number
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def game(level):
    score = 0
    # generate ten levels
    for _ in range(10):
        x, y = generate_integer(level)
        answer = x + y
        guess = str(input(f"{x} + {y} = "))
        # check if answer is incorrect
        if guess != str(answer):
            x2, y2 = x, y
            answer2 = x2 + y2
            incorrect = 1
            print("EEE")
            while incorrect != 3:
                guess2 = str(input(f"{x2} + {y2} = "))
                if guess2 == str(answer2):
                    score +=1
                    break
                else:
                    print("EEE")
                    incorrect += 1
            else:
                print(f"{x2} + {y2} = {answer2}")
        # check if answer is correct
        else:
            score += 1
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
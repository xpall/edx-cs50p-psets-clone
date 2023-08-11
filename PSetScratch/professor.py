from random import randint

digits = {1:10, 2:100, 3:1000}
digits_start = {1:0, 2:10, 3:100}

def main():
    level = get_level("Level: ")
    game(level)

def get_level(prompt):
    while True:
        try:
            prompt = int(input(prompt))
            if prompt in digits:
                return prompt
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    n = randint(digits_start[level], digits[level] - 1)
    return n

def game(level):
    correct = 0
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer_key = num1 + num2
        answer_key = str(answer_key)
        answer_player = str(input(f"{num1} + {num2} = "))

        if answer_player != answer_key:
            num1_error, num2_error = num1, num2
            fails = 2
            while fails != 0:
                print("EEE")
                fails -= 1
                answer_player2 = str(input(f"{num1_error} + {num2_error} = "))
                answer_key2 = num1_error + num2_error
                answer_key2 = str(answer_key2)
                if answer_key2 == answer_player2:
                    correct += 1
                    break
                else:
                    print(f"{num1_error} + {num2_error} = {answer_key2}")
        else:
            correct += 1

    print(f"{correct}")

if __name__ == "__main__":
    main()
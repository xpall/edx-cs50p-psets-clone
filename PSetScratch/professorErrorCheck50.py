import sys
import random

digits = {1:10, 2:100, 3:1000}
digits_start = {1:0, 2:10, 3:100}

def main():
    generate_integer(get_level("Level: "))

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
    while True:
        try:
            passes = 0
            ten_items = 0
            while ten_items != 10:
                x = random.randint(digits_start[level], digits[level] - 1)
                y = random.randint(digits_start[level], digits[level] - 1)
                answer_key = x + y
                answer_player = int(input(f"{x} + {y} = "))
                if answer_player != answer_key:
                    ten_items = ten_items + 1
                    x_error = x
                    y_error = y
                    fails = 2
                    while fails != 0:
                        print("EEE")
                        fails -= 1
                        answer_key2 = x_error + y_error
                        answer_player = int(input(f"{x_error} + {y_error} = "))
                    print("EEE")
                    print(f"{x_error} + {y_error} = {answer_key2}")
                elif answer_player == answer_key:
                    ten_items += 1
                    passes += 1
            else:
                print(f"{passes}")
                break
        except (KeyError, ValueError):
            break

if __name__ == "__main__":
    main()
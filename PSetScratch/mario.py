def main():
    num = int(input("Size of block n2: "))
    print_square(num)

def print_square(size):
    for i in range(size):
        print("#" * (size - 1))

main()
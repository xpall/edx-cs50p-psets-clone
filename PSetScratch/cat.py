def main():
    number = getNumber()
    meow(number)

def getNumber():
    while True:
        n = int(input("How many meows? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()
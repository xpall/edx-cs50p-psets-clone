def main():
    x = float(input("Enter a number: "))
    if parity_Test(x):
        print("Even")
    else:
        print("Odd")

def parity_Test(n):
    return n % 2 == 0

main()
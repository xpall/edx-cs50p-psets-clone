def main():
    expression = str(input("Enter an arithmetic expression: "))
    arithmetic = splitter(expression)
    answer = calcu(arithmetic)

def splitter(a):
    a = a.split(" ")
    return(a)

def calcu(a):
    x = float(a[0])
    z = float(a[2])
    op = a[1]
    if op == "+":
        print(round((x + z), 1))
    elif op == "-":
        print(round((x - z), 1))
    elif op == "/":
        print(round((x / z), 1))
    elif op == "*":
        print(round((x * z), 1))
    else:
        print("Error")

main()



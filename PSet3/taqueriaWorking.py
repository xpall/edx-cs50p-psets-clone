menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    cashier("Item: ")

def cashier(order):
    total = 0
    while True:
        try:
            x = input(order).title()
        except EOFError:
            print()
            break
        except KeyError:
            print()
            break
        if x in menu:
                price = float(menu[x])
                total = total + price
                totalprint = format(total, ".2f")
                print(f"Total: ${totalprint}")

main()
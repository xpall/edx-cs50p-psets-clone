price = 50

while price > 0:
    print("Amount Due:", price)
    payment = int(input("Insert coin: "))
    if payment in [5, 10, 25]:
        price -= payment

change = abs(price)
print("Change Owed:", change)
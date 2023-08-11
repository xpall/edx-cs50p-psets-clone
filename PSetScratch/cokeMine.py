price = 50

while price > 0:
    payment = int(input("Insert coin: "))
    if payment in [5, 10, 25]:
        price -= payment
        print("Amount due: ", price)

print("Change owed: ", abs(payment - price))
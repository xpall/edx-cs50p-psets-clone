class Item:
    def __init__(self, name: str, price: float, quantity= 0):
        self.name = name
        self.price = price
        self.quantity = quantity


    def selling_price(self):
        return self.price * self.quantity


    def __str__(self):
        return f"{self.name} is priced at {self.price}, availabe in {self.quantity} piece(s)"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(item1)
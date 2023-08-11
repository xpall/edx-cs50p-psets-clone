a = int(input("Input first number: "))
b = int(input("Input second number: "))
o = input("Operation: ")

if o == "+":
    c = a + b
elif o == "-":
    c = a - b
elif o == "/":
    c = a // b
elif o == "*":
    c = a * b
print(f"{a} {o} {b} is equal to {c}")
rounded = round(c,2)
print(f"The rounded version is {rounded:,}")
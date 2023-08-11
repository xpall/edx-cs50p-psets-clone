def main():
    gauge("Fuel: ")

def gauge(prompt):
    while True:
        try:
            x = str(input(prompt))
            x = x.split("/")
            a = int(x[0])
            b = int(x[1])
            x = round((a / b) * 100)
            if a > b:
                continue
            elif x <= 1:
                print("E")
            elif x >= 99:
                print("F")
            else:
                print(f"{round(x)}%")
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return

main()
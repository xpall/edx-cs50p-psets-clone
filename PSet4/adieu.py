def main():
    bye("Name: ")

def bye(prompt):
    name_list = []
    while True:
        try:
            name = str(input(prompt)).title()
            name_list.append(name)
        except EOFError:
            if len(name_list) == 1:
                print("Adieu, adieu, to " + ", ".join(name_list))
            elif len(name_list) == 2:
                print(f"Adieu, adieu, to " + " and ".join(name_list))
            else:
                name_last = name_list.pop(-1)
                print(f"Adieu, adieu, to " + ", ".join(name_list) + ", and " + (name_last))
            break

main()

def main():
    to_buy("")

def to_buy(prompt):
    items_list = []
    while True:
        try:
            item = str(input(prompt)).upper()
            items_list.append(item)
            items_list.sort()
        except EOFError:
            items_dict = {}
            for i in items_list:
                if i not in items_dict.keys():
                    items_dict[i] = 1
                else:
                    items_dict[i] = items_dict[i] + 1
            for i in items_dict:
                print(items_dict[i], i)
            break

main()
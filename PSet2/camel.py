text_list = list(str(input("camelCase: ")))
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in text_list:
    if char in capitals:
        position = int(text_list.index(char))
        text_list[position] = char.lower()   #required to get out of loop
        text_list.insert(position, "_")

print("".join(text_list))
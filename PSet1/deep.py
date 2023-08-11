def main():
    answer = str(input("What is the  answer to the Great Question of Life, the Universe and Everything? ")).lower().replace(" ","").replace("-","").replace(",","")
    if checker(answer) == True:
        print("Yes")
    else:
        print("No")

def checker(s):
    return s == "42" or s == "fortytwo"

main()
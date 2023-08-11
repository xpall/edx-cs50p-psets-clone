def main():
    greet = str(input("Greetings: ")).lower().strip().replace(" ","")
    if firstWordTest(str(greet)) == "hello":
        print("$0")
    elif firstLetterTest(str(greet)) == "h":
        print("$20")
    else:
        print("$100")

def firstWordTest(l):
    l = l[0:5]
    return(l)

def firstLetterTest(l):
    l = l[0]
    return(l)

main()
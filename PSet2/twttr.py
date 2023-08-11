def main():
    string = str(input("Your text: "))
    print(vowel_remover(string))

def vowel_remover(t):
    vowels = "aeiouAEIOU"
    for char in t:
        if char in vowels:
            t = t.replace(char,"")
    return t

main()
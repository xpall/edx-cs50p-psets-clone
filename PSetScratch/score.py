#import emoji
#str(print("Welcome to score conversion simple app :)")).replace("\:)","🙂")

score = int(input("Input score here: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
fruits_calories_content = {
    'Apple' : 130,
    'Avocado' : 50,
    'Banana' : 110,
    'Cantaloupe' : 50,
    'Grapefruit' : 60,
    'Grapes' : 90,
    'Honeydew' : 50,
    'Kiwifruit' : 90,
    'Lemon' : 15,
    'Lime' : 20,
    'Nectarine' : 60,
    'Orange' : 80,
    'Peach' : 60,
    'Pear' : 100,
    'Pineapple' : 50,
    'Plums' : 70,
    'Strawberries' : 50,
    'Sweet Cherries' : 100,
    'Tangerine' : 50,
    'Watermelon' : 80
    }
def main():
    fruit = str(input("Enter name of fruit: ")).title()
    amount_of_calories(fruit)

def amount_of_calories(x):
    if x in fruits_calories_content:
        calories = fruits_calories_content[x]
        print(f"Calories:", calories)
    else:
        x = ""
        print(x)
main()

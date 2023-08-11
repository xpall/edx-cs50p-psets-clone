import sys
import random
import pyfiglet

fontstyle = [
    '3-d',	'3x5',	'5lineoblique',	'acrobatic',	'alligator',	'alligator2',	'alphabet',	'avatar',	'banner',	'banner3-D',	'banner3',	'banner4',	'barbwire',	'basic',	'bell',	'big',	'bigchief',	'binary',	'block',	'bubble',	'bulbhead',	'calgphy2',	'caligraphy',	'catwalk',	'chunky',	'coinstak',	'colossal',	'computer',	'contessa',	'contrast',	'cosmic',	'cosmike',	'cricket',	'cursive',	'cyberlarge',	'cybermedium',	'cybersmall',	'diamond',	'digital',	'doh',	'doom',	'dotmatrix',	'drpepper',	'eftichess',	'eftifont',	'eftipiti',	'eftirobot',	'eftitalic',	'eftiwall',	'eftiwater',	'epic',	'fender',	'fourtops',	'fuzzy',	'goofy',	'gothic',	'graffiti',	'hollywood',	'invita',	'isometric1',	'isometric2',	'isometric3',	'isometric4',	'italic',	'ivrit',	'jazmine',	'jerusalem',	'katakana',	'kban',	'larry3d',	'lcd',	'lean',	'letters',	'linux',	'lockergnome',	'madrid',	'marquee',	'maxfour',	'mike',	'mini',	'mirror',	'mnemonic',	'morse',	'moscow',	'nancyj-fancy',	'nancyj-underlined',	'nancyj',	'nipples',	'ntgreek',	'o8',	'ogre',	'pawp',	'peaks',	'pebbles',	'pepper',	'poison',	'puffy',	'pyramid',	'rectangles',	'relief',	'relief2',	'rev',	'roman',	'rot13',	'rounded',	'rowancap',	'rozzo',	'runic',	'runyc',	'sblood',	'script',	'serifcap',	'shadow',	'short',	'slant',	'slide',	'slscript',	'small',	'smisome1',	'smkeyboard',	'smscript',	'smshadow',	'smslant',	'smtengwar',	'speed',	'stampatello',	'standard',	'starwars',	'stellar',	'stop',	'straight',	'tanja',	'tengwar',	'term',	'thick',	'thin',	'threepoint',	'ticks',	'ticksslant',	'tinker-toy',	'tombstone',	'trek',	'tsalagi',	'twopoint',	'univers',	'usaflag',	'wavy',	'weird'
]

def main():
    if len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage")
    if len(sys.argv) == 3:
        if str(sys.argv[1]) not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        if sys.argv[2] not in fontstyle:
            sys.exit("Invalid usage")
    text = str(input("Input: "))
    figletize(text)

def figletize(t):
    if len(sys.argv) == 1:
        random_font = random.choice(fontstyle)
        print(pyfiglet.figlet_format(t, font = random_font))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            print(pyfiglet.figlet_format(t, font = sys.argv[2]))

main()
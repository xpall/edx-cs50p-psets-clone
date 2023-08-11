import sys

from PIL import Image
from PIL import ImageOps


def main():
    arg1, arg2 = argv_checker()
    tshirt_overlay(arg1, arg2)


def argv_checker():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith((".png", ".jpg", ".jpeg")) or not sys.argv[2].endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1], sys.argv[2]

def tshirt_overlay(arg1, arg2):
    try:
        with Image.open(arg1) as im1:
            shirt = Image.open('shirt.png')
            cropped_im1 = ImageOps.fit(im1, shirt.size)
            cropped_im1.paste(shirt, box=None, mask=shirt)
            cropped_im1.save(arg2)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__=="__main__":
    main()
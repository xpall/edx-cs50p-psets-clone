import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r'^(?:<iframe ).*src="(.+?)"(?:.*)(?:</iframe>)$', s):
        extract_link = url.group(1)
        if vid_link := re.search(r'^(?:https?)?(?:://)?(?:www\.)?youtube\.com/embed/(.+)$', extract_link):
            # print(vid_link.group(1))
            return f"https://youtu.be/{vid_link.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ipv4 := re.search(r"^([0-9]{1,3})+\.([0-9]{1,3})+\.([0-9]{1,3})+\.([0-9]{1,3})+$", ip):
        if int(ipv4.group(1)) <= 255 and int(ipv4.group(2)) <= 255 and int(ipv4.group(3)) <= 255 and int(ipv4.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
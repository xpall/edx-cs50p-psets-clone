from twttr import shorten

def main():
    test_text()
    test_number()
    test_float()


def test_text():
    assert shorten("ass") == "ss"
    assert shorten("abcdEf") == "bcdf"


def test_number():
    assert shorten("1sEaUUx") == "1sx"

def test_float():
    assert shorten("1.e.,ixuasd") == "1..,xsd"

if __name__ == "__main__":
    main()
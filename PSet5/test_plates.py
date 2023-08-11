from plates import is_valid


def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("aA0") == False
    assert is_valid("01") == False
    assert is_valid("aa10") == True
    assert is_valid("11") == False
    assert is_valid("abcdef") == True
    assert is_valid("_ae3") == False
    assert is_valid("+zxc") == False
    assert is_valid("zxc1231") == False
    assert is_valid("asD21x") == False
    assert is_valid("zxc&_+") == False


if __name__ == "__main__":
    main()
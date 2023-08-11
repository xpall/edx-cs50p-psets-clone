from numb3rs import validate


def main():
    test_single_digits()
    test_notdigits()
    test_digits_not_in_range()
    test_invalids()


def test_single_digits():
    assert validate('1.1.1.1') == True


def test_notdigits():
    assert validate('a.2.3.2') == False
    assert validate('asdasd') == False


def test_digits_not_in_range():
    assert validate('255.0.1.256') == False
    assert validate('255.255.255.255') == True


def test_invalids():
    assert validate('a.b.c...') == False
    assert validate('1.2..2') == False
    assert validate('255.23.2') == False
    assert validate('1.1.1.1.1') == False


if __name__=="__main__":
    main()
from bank import value


def main():
    test_hello()
    test_with_h()
    test_h_only()
    test_no_h()
    test_case_sensitive1()
    test_case_sensitive2()

def test_hello():
    assert value("hello") == 0


def test_with_h():
    assert value("hello hello hello") == 0


def test_h_only():
    assert value("hhahaha") == 20


def test_no_h():
    assert value("enloooo") == 100


def test_case_sensitive1():
    assert value("HELLO") == 0


def test_case_sensitive2():
    assert value("hEllPMeee") == 20


if __name__ == "__main__":
    main()
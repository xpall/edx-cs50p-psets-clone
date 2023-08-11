from um import count


def main():
    test_valid()
    test_uppercase()
    test_um_inside_words()
    test_symbols_after_um()
    #test_symbols_before_um()
    test_multiple_ums()
    test_no_ums()
    test_symbol_after_ums()

def test_valid():
    assert count("um, hello, um, world") == 2


def test_uppercase():
    assert count("Um, uM hello, UM, world") == 3


def test_um_inside_words():
    assert count("yummy, umy") == 0
    assert count("ummm") == 0


def test_symbols_after_um():
    assert count("hello, um, um?") == 2
    assert count("um!!!!") == 1

# def test_symbols_before_um():
#     assert count("hello, ?um, !um") == 0


def test_multiple_ums():
    assert count("um, UM, Um, uM, ,um,") == 5


def test_no_ums():
    assert count("mewmew") == 0
    assert count("yumyumyum!") == 0


def test_symbol_after_ums():
    assert count("um!, um?, um.") == 3

if __name__=="__main__":
    main()
import pytest
from fuel import convert
from fuel import gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()
import pytest
from working import convert


def main():
    test_valid()
    test_wrong_hours()
    test_pm()
    test_am()
    test_invalid_time_format()


def test_valid():
    assert convert('9 AM to 6 PM') == '09:00 to 18:00'


def test_wrong_hours():
    with pytest.raises(ValueError):
        assert convert('13:60 AM to 5:00 PM')

def test_wrong_format():
    with pytest.raises(ValueError):
        assert convert('9:60 AM 5:00 PM')

def test_invalid_time_format():
    with pytest.raises(ValueError):
        assert convert("9-00 AM to 5-00 PM")

def test_pm():
    assert convert('4 PM to 11:12 PM') == '16:00 to 23:12'


def test_am():
    assert convert('4 AM to 11:12 AM') == '04:00 to 11:12'


if __name__=="__main__":
    main()
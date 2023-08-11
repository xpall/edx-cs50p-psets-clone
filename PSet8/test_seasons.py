import pytest
from seasons import get_valid_birthdate


def main():
    test_invalid_date()
    # test_valid()

def test_invalid_date():
    with pytest.raises(SystemExit):
        assert get_valid_birthdate('10-31-1997')

# def test_valid():
#     assert get_valid_birthdate('2022-04-06') == 'Five hundred twenty-five thousand, six hundred minutes'


if __name__ == "__main__":
    main()
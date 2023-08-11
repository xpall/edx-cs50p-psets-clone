import pytest
from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    test_value_error()


def test_init():
    jar = Jar(100)


def test_str():
    jar_str = Jar(20)
    jar_str.deposit(5)
    assert str(jar_str) == '🍪🍪🍪🍪🍪'


def test_deposit():
    jar_deposit = Jar(10)
    jar_deposit.deposit(5)
    jar_deposit.size == 5


def test_withdraw():
    jar_withdraw = Jar(10)
    jar_withdraw.deposit(8)
    jar_withdraw.withdraw(2)
    jar_withdraw.size == 6


def test_value_error():
    with pytest.raises(ValueError):
        assert Jar(0)
        assert Jar(-10)
        jar_value_error = Jar(5)
        assert jar_value_error.withdraw(10)


if __name__ == "__main__":
    main()
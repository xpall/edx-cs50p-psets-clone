from professor2_frustrating import get_level, generate_integer


def main():
    test_invalid_level()
    test_wrong_answer()
    test_correct_answer()
    test_string()
    test_negative()


def test_invalid_level():
    assert get_level(-1) == "Level: "

if __name__ == "__main__":
    main()
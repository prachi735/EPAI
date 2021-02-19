import pytest
from assignment_2 import *


shift_char_tests = [
    ("abyz", -1, "zaxy"),
    ("ATTACKATONCE", 4, "EXXEGOEXSRGI"),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23, 'XYZABCDEFGHIJKLMNOPQRSTUVW')
]


@pytest.mark.parametrize("input, shift, expected", shift_char_tests)
def test_shift_char(input, shift, expected):
    assert shift_char(input, shift) == expected.lower()


swear_words_tests = [
    ("yo bitch ja rule is more succesful then you ll ever be whats up with you and hating you sad mo fuck...", True), ("from rfc the title is fine as it is imo", False)]


@pytest.mark.parametrize("input, expected", swear_words_tests)
def test_check_swear_words(input: str, expected: bool):
    assert check_swear_words(input)[0] == expected


add_even_tests = [
    ([1, 2, 3, 4, 5, 6], 12),
    ([], 0),
    ([-2, -5], -2)]


@pytest.mark.parametrize("input, expected", add_even_tests)
def test_add_even(input, expected):
    assert add_even(input) == expected


max_char_tests = [
    ("ABCD123", "D"), ("azse", "z")]


@ pytest.mark.parametrize("input, expected", max_char_tests)
def test_max_char(input, expected):
    assert max_char(input) == expected


add_3rd_element_tests = [([1, 2, 3, 4, 5, 6], 9)]


@ pytest.mark.parametrize("input, expected", add_3rd_element_tests)
def test_add_3rd_element(input, expected):
    assert add_3rd_element(input) == expected

    #     _tests = [
    # (,), (, ]
    #     @ pytest.mark.parametrize("input, expected", _tests)
    #     def test_random_license_number_1(input, expected):
    # pass

    #     _tests=[
    # (,), (, ]
    #     @ pytest.mark.parametrize("input, expected", _tests)
    #     def test_random_license_number_2(input, expected):
    # pass

    #     _tests=[
    # (,), (, ]
    #     @ pytest.mark.parametrize("input, expected", _tests)
    #     def random_license_number_3():
    # pass

import closure_assignment
from closure_assignment import *
import pytest
import re
import inspect
import os


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme_words = [word for line in open(
        'README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(
        readme_words) >= 200, "Add some description to README.md file!"


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(closure_assignment)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(closure_assignment, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def function_sh_docstring() -> None:
    """ This is a dummy function with short docstring"""
    pass


def function_lg_docstring() -> None:
    """ This is a dummy function with long docstring.
    This is a dummy function with long docstring
    This is a dummy function with long docstring
    This is a dummy function with long docstring
    This is a dummy function with long docstring
    """
    pass


check_docstring_testcases = [('valid', function_sh_docstring, False), (
    'valid', function_lg_docstring, True), ('error', None, TypeError)]


@pytest.mark.parametrize("case, func_name, expected", check_docstring_testcases)
def test_check_docstring(case, func_name, expected):
    docstring_valid = check_docstring(50)
    if case == 'valid':
        assert docstring_valid(
            func_name) == expected, "Making sure your function has proper description"
    elif case == 'error':
        with pytest.raises(expected):
            docstring_valid(func_name), "Check docstring for a function....."


def test_get_next_fibonacci():
    new_fibonacci = get_next_fibonacci()
    assert new_fibonacci() == 0


def test_get_next_fibonacci():
    new_fibonacci = get_next_fibonacci()
    new_fibonacci()
    assert new_fibonacci() == 1


def test_func_call_counter_0():
    fibonacci_counter = func_call_counter(get_next_fibonacci)
    assert fibonacci_counter.calls == 0


def test_func_call_counter():
    fibonacci_counter = func_call_counter(get_next_fibonacci())
    for i in range(9):
        fibonacci_counter()
    assert fibonacci_counter.calls == 9


def test_func_call_counter_dict_0():
    add_calls = func_call_counter_dict(add)
    mul_calls = func_call_counter_dict(mul)
    div_calls = func_call_counter_dict(div)
    assert add_calls.calls == 0 and mul_calls.calls == 0 and div_calls.calls == 0 and func_call_count == {
        'add': 0, 'mul': 0, 'div': 0}


def test_func_call_counter_dict_1():
    add_calls = func_call_counter_dict(add)
    mul_calls = func_call_counter_dict(mul)
    div_calls = func_call_counter_dict(div)
    (add_calls(1, 2))
    assert add_calls.calls == 1 and mul_calls.calls == 0 and div_calls.calls == 0 and func_call_count == {
        'add': 1, 'mul': 0, 'div': 0}


def test_func_call_counter_dict_all():
    add_calls = func_call_counter_dict(add)
    mul_calls = func_call_counter_dict(mul)
    div_calls = func_call_counter_dict(div)
    (add_calls(1, 2))
    (mul_calls(3, 4))
    (div_calls(5, 6))
    (add_calls(9, 1))
    assert add_calls.calls == 2 and mul_calls.calls == 1 and div_calls.calls == 1 and func_call_count == {
        'add': 2, 'mul': 1, 'div': 1}


def test_all_func_call_counter():
    math_dict = {}
    fib_dict = {}
    add_calls = all_func_call_counter(add, math_dict)
    mul_calls = all_func_call_counter(mul, math_dict)
    fib_calls = all_func_call_counter(get_next_fibonacci, fib_dict)
    (mul_calls(3, 4))
    (add_calls(9, 1))
    (add_calls(10, 1))
    fib_calls()
    fib_calls()
    assert math_dict == {'mul': 1, 'add': 2} and fib_dict == {
        'get_next_fibonacci': 2}

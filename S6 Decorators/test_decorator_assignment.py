import pytest
import decorator_assignment
from decorator_assignment import *
import os
import re
import inspect
from time import strftime


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
    lines = inspect.getsource(decorator_assignment)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(decorator_assignment, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


@run_at_odd_seconds_only
def add(a, b):
    return a+b


def test_run_at_odd_seconds_only():
    if int(strftime('%S')) % 2 == 0:
        assert add(1, 2) == 3
    else:
        assert add(1, 2) == None


@timed(10)
def my_repeating_fun():
    return "Repeated"


def test_timed():
    from time import perf_counter
    my_repeating_fun()
    # start = perf_counter()
    # for _ in range(10):
    #     my_repeating_fun.__wrapped__()
    # avg_run_time = (perf_counter() - start)/10
    # and my_repeating_fun.avg_run_time == avg_run_time
    assert my_repeating_fun.calls == 10


@authenticate('user', 'pwd')
def my_auth_fun():
    return "You have been authenticated to run me!!!!!"


@authenticate('user_d', 'pwd_d')
def my_auth_fun2():
    return "You have been authenticated to run me!!!!!"


authenticate_testcases = [(my_auth_fun, 'You have been authenticated to run me!!!!!'),
                          (my_auth_fun2, 'Authentication Failed!!!')]


@pytest.mark.parametrize(('func, expected'), authenticate_testcases)
def test_authenticate(func, expected):
    assert func() == expected


@has_privilege('high')
def high_privi_func(*args):
    return (args)


@has_privilege('mid')
def mid_privi_func(*args):
    return (args)


@has_privilege('low')
def low_privi_func(*args):
    return (args)


@has_privilege('no')
def no_privi_func(*args):
    return (args)


has_privilege_testcases = [(high_privi_func, ('param1', 'param2', 'param3', 'param4')), (mid_privi_func, ('param1', 'param2', 'param3')),
                           (low_privi_func, ('param1', 'param2')), (no_privi_func, ('param1',))]

@pytest.mark.parametrize("func,expected",has_privilege_testcases)
def test_has_privilege(func,expected):
    assert func() == expected

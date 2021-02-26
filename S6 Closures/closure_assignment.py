from numbers import Number
from typing import DefaultDict

fibonacci_list = []


def check_docstring(doc_string_min_len: int = 30) -> bool:
    """check if the function has a doctring"""

    def doc_string(func: callable):
        if callable(func):
            return len(func.__doc__) > doc_string_min_len
        else:
            raise TypeError("Pass a valid function as an argument.")

    return doc_string

def get_next_fibonacci() -> int:
    """
    This function updated a global list of fibonacci numbers and returns the last number from the list
    """
    def fibonacci():
        global fibonacci_list
        if fibonacci_list == []:
            fibonacci_list = [0]
        elif fibonacci_list == [0]:
            fibonacci_list = [0, 1]
        else:
            fib_len = len(fibonacci_list)
            fibonacci_list += [fibonacci_list[fib_len-1] + fibonacci_list[fib_len-2]]
        return fibonacci_list[-1]

    return fibonacci


def func_call_counter(func: callable):
    """
    This function add a call attribute to the function 
    that gives the number of times the function has been called
    """
    def counter(*args, **kwargs):
        counter.calls += 1
        return func(*args, **kwargs)
    counter.calls = 0
    if callable(func):
        counter.__name__ = func.__name__
        return counter
    else:
        raise TypeError("Pass a valid function as an argument.")

def add(num1: Number, num2: Number) -> Number:
    """
    This is a simple function to add 2 numbers
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1+num2
    else:
        raise TypeError("Can only add numbers!!!")


def mul(num1: Number, num2: Number) -> Number:
    """
    This is a simple function to multiply 2 numbers
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1*num2
    else:
        raise TypeError("Can only multiply numbers!!!")


def div(num: Number, den: Number) -> Number:
    """
    This is a simple function to divide 2 numbers
    """
    if isinstance(num, (int, float)) and isinstance(den, (int, float)):
        if den != 0:
            return num/den
        else:
            raise ValueError("Cannot divide by zero.....")
    else:
        raise TypeError("Can only divide numbers!!!")


func_call_count = {add.__name__: 0, mul.__name__: 0, div.__name__: 0}


def func_call_counter_dict(func: callable):
    """
    This function add a call attribute to the function 
    that gives the number of times the function has been called 
    and also updates a global dictionary with number of times the function has been called
    """

    def counter(*args, **kwargs):
        counter.calls += 1
        func_call_count[func.__name__] = counter.calls
        return func(*args, **kwargs)

    counter.calls = 0
    if callable(func) and func.__name__ in func_call_count.keys():
        counter.__name__ = func.__name__
        return counter
    else:
        raise TypeError("Pass a valid function as an argument. Function can be add, mul, div.")


def all_func_call_counter(func: callable, func_count: dict) -> dict:
    """
    This function add a call attribute to the function 
    that gives the number of times the function has been called 
    and also updates the given dictionary with number of times the function has been called
    """

    def counter(*args, **kwargs):
        counter.calls += 1
        func_count[func.__name__] = counter.calls
        return func(*args, **kwargs)

    counter.calls = 0
    if callable(func):
        counter.__name__ = func.__name__
        return counter
    else:
        raise TypeError("Pass a valid function as an argument.")


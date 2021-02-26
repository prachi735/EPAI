## Assignment Objective
The asignment objective is to understand closures in Python
The poject contains below closures:

    1. check_docstring: a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable
    definition: check_docstring(doc_string_min_len: int = 30) -> bool
    example:
            docstring_valid = check_docstring(50)

            def function_sh_docstring() -> None:
            """ This is a dummy function"""
            pass

            docstring_valid(func_name) # return false

    2. get_next_fibonacci: a closure that gives you the next Fibonacci number
    definition: get_next_fibonacci() -> int
    example:
            new_fibonacci = get_next_fibonacci()
            new_fibonacci() # returns 0 
            new_fibonacci() # returns 1
            new_fibonacci() # returns 1
            new_fibonacci() # returns 2
            new_fibonacci() # returns 3
            new_fibonacci() # returns 5

    3. func_call_counter: a closure that counts how many times a function was called. 
    definition: func_call_counter(func: callable
    example:
            fibonacci_counter = func_call_counter(get_next_fibonacci())
            fibonacci_counter()
            fibonacci_counter()
            fibonacci_counter.calls # returns 2

    4. func_call_counter_dict: a closure that can keep a track of how many times add/mul/div functions were called, and updates a global dictionary variable with the counts 
    definition: func_call_counter_dict(func: callable)
    example:
            add_calls = func_call_counter_dict(add)
            mul_calls = func_call_counter_dict(mul)
            div_calls = func_call_counter_dict(div)
            add_calls(1, 2)
            mul_calls(3, 4)
            div_calls(5, 6)
            add_calls(9, 1)
            print(func_call_count) # prints{'add': 2, 'mul': 1, 'div': 1})

    5. all_func_call_counter: above closure is modified such that now we can pass in different dictionary variables to update different dictionaries
    definition: all_func_call_counter(func: callable, func_count: dict) -> dict
    example:
            math_dict = {}
            fib_dict = {}
            add_calls = all_func_call_counter(add, math_dict)
            mul_calls = all_func_call_counter(mul, math_dict)
            fib_calls = all_func_call_counter(get_next_fibonacci, fib_dict)
            mul_calls(3, 4)
            add_calls(9, 1)
            add_calls(10, 1)
            fib_calls()
            fib_calls()
            print(math_dict) # prints {'mul': 1, 'add': 2} 
            print(fib_dict) # prints {'get_next_fibonacci': 2}


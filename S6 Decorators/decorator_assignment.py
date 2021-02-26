import logging
import functools
import os
import re
import sys
import logging
from time import strftime
from functools import wraps

from _pytest.mark import param


def run_at_odd_seconds_only(func: callable):
    r"""allows a function to run only on odd seconds"""
    def run_if_odd_sec(*args, **kwargs):
        if int(strftime('%S')) % 2 == 0:
            return func(*args, **kwargs)
    return run_if_odd_sec


logger = logging.getLogger()


def create_log(fn:callable()):
    r"""the adds below information to the logger object about the function:
        a. When we are entering the function
        b. The value returned by the function
        c. When we are exiting the function"""
    @wraps(fn)
    def log(*args, **kwargs):
        logger.info("Entering {:s}...".format(fn.__name__))
        try:
            result = fn(*args, **kwargs)
            logger.info("Return Value:", result)
        except:
            logger.error("Exception:", sys.exc_info()[0])
            raise
        logger.info("Finished {:s}.".format(fn.__name__))
        return result

    return log


def get_user_and_password():
    return 'user', 'pwd'


def authenticate(username:str, password:str):
    r"""allows the function to be run if the user is authenticated """
    def validate_auth(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            auth_user, auth_pwd = get_user_and_password()
            if auth_user == username and auth_pwd == password:
                return func(*args, **kwargs)
            else:
                return "Authentication Failed!!!"
        return decorated
    return validate_auth


def timed(n:int):
    r"""adds an attribute 'avg_run_time' to the function that gives the average run time of the function"""
    from time import perf_counter

    def n_times(func: callable):
        @wraps(func)
        def repeat(*args, **kwargs):
            start = perf_counter()
            for _ in range(n):
                repeat.calls += 1
                value = func(*args, **kwargs)
            repeat.avg_run_time = (perf_counter() - start)/n
            return value
        repeat.calls = 0
        repeat.avg_run_time = 0
        return repeat
    return n_times


def has_privilege(privilege:str):
    r"""
    Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
    """
    param1 = 'param1'
    param2 = 'param2'
    param3 = 'param3'
    param4 = 'param4'

    def access(func):
        @wraps(func)
        def f_call(*args, **kwargs):
            if privilege == 'high':
                return func(param1, param2, param3, param4, *args, **kwargs)
            if privilege == 'mid':
                return func(param1, param2, param3, *args, **kwargs)
            if privilege == 'low':
                return func(param1, param2, *args, **kwargs)
            if privilege == 'no':
                return func(param1, *args, **kwargs)
        return f_call
    return access

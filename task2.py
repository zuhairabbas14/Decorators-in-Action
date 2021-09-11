import inspect
import os
import sys
import time


def decorator_2(func):
    def get_info(*args, **kwargs):
        get_info.calls += 1
        sys.stdout = open(os.devnull, 'w')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        sys.stdout = sys.__stdout__
        print(func.__name__, ' call {} executed in {} sec'.format(get_info.calls, round(end - start, 4)))
        print('Name:', func.__name__)
        print('Type:', type(func))
        print('Sign:', func.__code__.co_varnames)
        print('Args:', 'positional', args, 'key=worded', kwargs)
        print('Doc:', func.__doc__)
        print('Source:', inspect.getsource(func))
        print('Output:')
        print(func(*args, **kwargs))

    get_info.calls = 0
    return get_info

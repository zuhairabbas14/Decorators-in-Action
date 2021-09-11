import os
import sys
import time


def decorator_1(func):
    def get_info(*args, **kwargs):
        get_info.calls += 1
        sys.stdout = open(os.devnull, 'w')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        sys.stdout = sys.__stdout__
        print(func.__name__, 'call {} executed in {} sec'.format(get_info.calls, round(end - start, 4)))

    get_info.calls = 0
    return get_info

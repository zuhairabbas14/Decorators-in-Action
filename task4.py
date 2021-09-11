import datetime
import inspect
import os
import sys
import time


def function_decorator(func):
    def get_info(*args, **kwargs):
        ct = datetime.datetime.now()
        get_info.calls += 1
        sys.stdout = open(os.devnull, 'w')
        start = time.time()

        try:
            func(*args, **kwargs)
        except Exception as e:
            sys.stdout = open('logs.log', 'w')
            print('Timestamp:', ct, '\nException:', e)
            sys.stdout.close()
            return

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
        func(*args, **kwargs)

    get_info.calls = 0
    return get_info


class ClassDecorator:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        self._time = 0.0
        self.ct = datetime.datetime.now()

    def __call__(self, *args, **kwargs):
        self.calls += 1
        sys.stdout = open(os.devnull, 'w')
        start = time.time()

        try:
            self.func(*args, **kwargs)
        except Exception as e:
            sys.stdout = open('logs.log', 'w')
            print('Timestamp:', self.ct, '\nException:', e)
            sys.stdout.close()
            return

        end = time.time()
        self._time = end - start
        sys.stdout = sys.__stdout__

        with open('output.txt', 'w') as f:
            f.write("%s\n" % (self.func.__name__ + ' call {} executed in {} sec'.format(self.calls, round(end - start, 4))))
            f.write("%s\n" % ('Name: ' + self.func.__name__))
            f.write("%s\n" % ('Type: ' + str(type(self.func))))
            f.write("%s\n" % ('Sign: ' + str(self.func.__code__.co_varnames)))
            f.write("%s\n" % ('Args: ' + 'positional ' + str(args) + ' key=worded ' + str(kwargs)))
            f.write("%s\n" % ('Doc: ' + str(self.func.__doc__)))
            f.write("%s\n" % ('Source: ' + str(inspect.getsource(self.func))))

        return self._time

import inspect
import os
import sys
import time


class Decorator:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        self._time = 0.0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        sys.stdout = open(os.devnull, 'w')
        start = time.time()
        self.func(*args, **kwargs)
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

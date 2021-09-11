import random
import time
import math
from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator
from task4 import function_decorator, ClassDecorator


@Decorator
def func1(a, b, c):  # test function 1
    time.sleep(0.2)
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


@Decorator
def func2(n: int):  # test function 2
    time.sleep(0.1)
    arr = [[0 for x in range(n)]
           for y in range(n)]

    for line in range(0, n):
        for i in range(0, line + 1):
            if i is 0 or i is line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")
            else:
                arr[line][i] = (arr[line - 1][i - 1] + arr[line - 1][i])
                print(arr[line][i], end=" ")
        print("\n", end="")


@Decorator
def func3(num):  # test function 3
    time.sleep(0.3)
    return lambda x: x * num


@Decorator
def func4(lst):  # test function 4
    time.sleep(0.4)
    filtered_list = list(filter(lambda num: (num > 7), lst))
    return filtered_list


if __name__ == "__main__":

    time1 = func1(1, 2, 3)
    time2 = func2(10)
    time3 = func3(14)
    time4 = func4([1, 7, 12, 2, 10, 99])

    functions = ['func1', 'func2', 'func2', 'func4']
    times = [time1, time2, time3, time4]
    ranked = sorted(zip(functions, times), key=lambda t: t[1])
    dic = {i: ranked[i] for i in range(len(ranked))}

    print()
    print("{:<6} {:<3} {:<6} {:<3} {:<6}".format('PROGRAM', '|', 'RANK', '|', 'TIME ELAPSED'))
    print()
    for k, v in dic.items():
        print("{:<11} {:<10} {:<10}".format(v[0], k, v[1]))

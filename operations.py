from functools import reduce


def add(*args):
    return reduce(lambda x, y: x+y, *args)


def sub(*args):
    return reduce(lambda x, y: x-y, *args)


def multiply(*args):
    return reduce(lambda x, y: x*y, *args)


def divide(*args):
    return reduce(lambda x, y: x/y, *args)


if __name__ == '__main__':
    print(add([1, 2, 3, 4, 5]))
    print(multiply([1, 2, 3, 4, 5]))
    print(divide([1, 2, 3, 4, 5]))
    print(sub([1, 2, 3, 4, 5]))
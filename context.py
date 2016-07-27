from operations import add
from operations import multiply
from operations import sub
from operations import divide


def log(*args):
    if len(*args) == 1:
        print(*args[0])
    else:
        print(*args)


context = {
    'log': log,
    '+': add,
    '*': multiply,
    '-': sub,
    '/': divide,
}

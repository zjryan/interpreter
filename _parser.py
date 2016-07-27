from stack import Stack
from stack import EmptyStackError
from context import context


def eval_elem(elem):
    if elem in context:
        val = elem
    else:
        val = eval(elem)
    return val


class InvalidParameters(Exception):
    pass


def get_right_internal(array, l):
    array_len = len(array)
    stack = Stack()
    if array[l] != '(':
        raise InvalidParameters("array[l] needs to be '('")

    i = l
    while not stack.is_empty() or i < array_len:
        elem = array[i]
        if elem == '(':
            stack.push(elem)
        elif elem == ')':
            try:
                stack.pop()
            except EmptyStackError:
                raise SyntaxError("unclosed parentheses, missing '('")
            if stack.is_empty():
                return i
        i += 1

    if stack.is_empty():
        return i
    else:
        raise SyntaxError("unclosed parentheses, missing ')'")


def get_ast(array, l=0):
    r = get_right_internal(array, l)
    i = l + 1
    ast = []
    while i < r:
        elem = array[i]
        if elem == '(':
            elem = get_ast(array, i)
            right = get_right_internal(array, i)
            i = right
        if type(elem) != list:
            elem = eval_elem(elem)
        ast.append(elem)
        i += 1
    return ast


# parser 输入符号列表得到抽象语法树
def parser(array):
    ast = get_ast(array)
    return ast


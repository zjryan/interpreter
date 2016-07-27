from _lexer import lexer
from _parser import parser
from _eval_ast import eval_ast


def calculator(code):
    chars = lexer(code)
    ast = parser(chars)
    val = eval_ast(ast)
    return val


def main():
    print('a simple lisp interpreter v0.1')
    while(True):
        code = input('> ')
        val = calculator(code)
        if val is not None:
            print(val)


if __name__ == '__main__':
    main()

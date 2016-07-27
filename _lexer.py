code = '(+ 132 2 (- 2 4))'


def lexer(code):
    code = code.replace('(', ' ( ')
    code = code.replace(')', ' ) ')
    array = code.split()
    return array


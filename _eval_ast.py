from context import context


def eval_ast(ast):
    operator, operands = ast[0], ast[1:]
    operands_num = len(operands)
    for i in range(0, operands_num):
        elem = operands[i]
        if type(elem) == list:
            operands[i] = eval_ast(elem)
    val = context[operator](operands)
    return val



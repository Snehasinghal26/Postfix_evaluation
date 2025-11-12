def createStack():
    stack = []
    return stack

def popStack(stack):
    if len(stack) == 0:
        return None
    return stack.pop()

def pushStack(stack, symbol):
    stack.append(int(symbol))

def evalPostfixExpr(expr):
    stack = createStack()
    operators = ['+', '-', '*', '/']
    for symbol in expr:
        if symbol in operators:
            operand2 = popStack(stack)
            operand1 = popStack(stack)
            if symbol == '+':
                result = operand1 + operand2
            elif symbol == '-':
                result = operand1 - operand2
            elif symbol == '*':
                result = operand1 * operand2
            elif symbol == '/':
                result = operand1 / operand2
            pushStack(stack, result)
        else:
            pushStack(stack, symbol)
    result = popStack(stack)
    return result

expr = input('Enter a postfix expression: ')
result = evalPostfixExpr(expr.split())
print("Result of evaluation of expression:", result)

# Write a Python program that simulates a handheld calculator. Your program
# should process input from the Python console representing buttons that are# "pushed", and then output the contents of the screen after each operation
# is performed. Minimally, your calculator should be abl to process the
# basic arithmetic operations and a reset/clear operation.

import math

if __name__ == '__main__':
    unary_op =  {
                    '!'     : lambda x: math.factorial(x),
                    'log10' : lambda x: math.log10(x),
                    'sqrt'  : lambda x: math.sqrt(x)
                }
    binary_op = { 
                    '^'     : lambda x, y: math.pow(x, y),
                    '+'     : lambda x, y: x + y,
                    '-'     : lambda x, y: x - y,
                    '*'     : lambda x, y: x * y,
                    '/'     : lambda x, y: x / y
                }
    operand = int(input('Enter an operand: '))
    operation = ''
    op_list = []
    op_list.append(operand)
    while operation != '=':
        operation = input('Enter operation: ')
        if operation in unary_op:
            result = unary_op.get(operation)(op_list[0])
            op_list[0] = result
            print('Current result:', result)
        elif operation in binary_op:
            next_operand = int(input('Enter next operand: '))
            op_list.append(next_operand)
            result = binary_op.get(operation)(op_list[0], op_list[1])
            print('Current result:', result)
            op_list[0] = result
            del op_list[1]
        elif operation == 'clear':
            op_list.clear()
            operation = ''
            operand = input('Enter an operand: ')
    print('Final result: ', result)

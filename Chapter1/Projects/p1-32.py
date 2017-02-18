# Write a Python program that can simulate a simple calculator, using the console as the exclusiveinput and output device.
# That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input, you should output to the Python console what would be displayed on your calc.

if __name__ == '__main__':
    operand1 = int(input('Enter 1st operand: '))
    operation = input('Enter operation: ')
    number_list = []
    number_list.append(operand1)
    binary_operations = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y
                 }
    while operation != '=':
        operand2 = int(input('Enter next operand: '))
        number_list.append(operand2)
        if operation in binary_operations:
            current_result = binary_operations.get(operation)(number_list[0], number_list[1])
            print('Current result:', current_result)
            number_list[0] = current_result
            del number_list[1]
        operation = input('Enter next operation: ')
    print('Final result:', current_result)
    

    
         

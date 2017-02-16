# Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula in the given order.
# EXAMPLE
# a + b = c
# a = b - c
# a * b = c

#import operator

def apply_func(num1, num2, num3):
    if num1 + num2 == num3:
        print(num1, '+', num2, '=', num3)
    elif num1 - num2 == num3:
        print(num1, '-', num2, '=', num3)
    elif num1 * num2 == num3:
        print(num1, '*', num2, '=', num3)
    elif num1 // num2 == num3:
        print(num1, '//', num2, '=', num3)

a = int(input('Input an integer for a: '))
b = int(input('Input an integer for b: '))
c = int(input('Input an integer for c: '))

apply_func(a, b, c)

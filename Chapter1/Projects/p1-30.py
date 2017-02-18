# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.

def count_num_2s(n):
    count = 0
    while n >= 2:
        n //=  2
        count += 1
    return count

if __name__ == '__main__':
    int_input = int(input('Enter a number greater than 2: '))
    print(count_num_2s(int_input))

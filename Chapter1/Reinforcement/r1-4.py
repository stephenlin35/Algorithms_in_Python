def sum_of_squares(n):
    """ Function that takes a positive integer n and returns the sum of the squares if all positive integers smaller than n. """

    if n < 1:
        return "Sorry, n must be a positive integer."
    sum = 0
    i = 1
    while i < n:
        i_sq = i * i
        sum += i_sq
        i += 1
    return sum

if __name__ == '__main__':
    print(sum_of_squares(2))
    print(sum_of_squares(3))
    print(sum_of_squares(5))

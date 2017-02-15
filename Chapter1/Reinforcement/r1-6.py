def squares_of_odds(n):
    """ Function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n. """

    sum = 0
    for i in range(n):
        if i & 1 == 1:          # use bitwise AND to check if num is odd
            i_sq = i * i
            sum += i_sq
    return sum

if __name__ == '__main__':
    print(squares_of_odds(2))
    print(squares_of_odds(5))

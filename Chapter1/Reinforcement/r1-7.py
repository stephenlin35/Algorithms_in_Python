def squares_of_odds(n):
    """ Single command function that computes the sum from r1-6, relying on Python's comprehension syntax and the built-in sum function. """

    return sum([i * i for i in range(n) if i & 1 == 1])

if __name__ == '__main__':
    print(squares_of_odds(2))
    print(squares_of_odds(5))

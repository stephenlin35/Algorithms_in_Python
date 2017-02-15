def get_squares(n):
    """ Single command that computes the sum from r1-4, relying on Python's comprehension syntax and the built-in sum function. """

    return sum([i * i for i in range(n)])

if __name__ == '__main__':
    print(get_squares(2))
    print(get_squares(3))
    print(get_squares(5))


def is_even(k):
    """ Funcion that takes an integer value and returns True if it is even,
    and False otherwise """

    if k & 1 == 0:          # uses bitwise & to check if even
        return True         
    return False

if __name__ == '__main__':
    print(is_even(25))
    print(is_even(1))
    print(is_even(100))

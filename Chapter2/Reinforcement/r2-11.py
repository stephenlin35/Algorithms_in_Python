# In section 2.3.3, we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, -2, 1], in which the sum of a vector and list returns a# new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is illegal. 
# Explain how the Vector class definition can be revised so that this syntax # generates a new vector.

class Vector:
    """ Represent a vector in a multidimensional space. """
    
    def __init__(self, d):
        """ Create a d-dimensional vector of zeroes. """
        self._coords = [0] * d

    def __len__(self):
        """ Return the dimension of the vector. """
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of vector. """
        return self._coords[j]

    def __setitem__(self, j, val):
        """ Set jth coordinate of vector to given value. """
        self._coords[j] = val

    def __add__(self, other):
        """ Return sum of two vectors. """
        if len(self) != len(other):         # relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))          # start with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        """ Return True if vector has same coordinates as other. """
        return self._coords == other._coords

    def __ne__(self, other):
        """ Return True if vector differs from other. """
        return not self == other            # rely on existing __eq__ def

    def __str__(self):
        """ Produce string representation of vector. """
        return '<' + str(self._coords)[1:-1] + '>'



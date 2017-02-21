# Implement the __sub__ method for the Vector class of SEction 2.3.3, so 
# that the expression u-v returns a new vector instance representing the
# difference between two vectors.

def __sub__(self, other):
    """ Return the difference of two vectors. """
    if len(self) != len(other):
        raise ValueError('Dimensions must agree')
    result = Vector(len(self))
    for i in range(len(self)):
        result[i] = self[i] - other[i]
    return result


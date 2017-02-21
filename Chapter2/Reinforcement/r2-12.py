# Implement the __mul__ method for the Vector class of Section 2.3.3, so 
# that the expression v * 3 returns a new vector with coordinates that are
# 3 times the respective coordinates of v.

class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)
    
    def __mul__(self, num):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * num
        return result
    
    def __rmul__(self, num):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * num
        return result

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, new_val):
        self._coords[i] = new_val

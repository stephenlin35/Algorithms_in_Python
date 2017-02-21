class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, new_value):
        self._coords[j] = new_value

    def __mul__(self, other):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * other[i]
        return result



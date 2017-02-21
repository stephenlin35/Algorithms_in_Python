# Implement the __neg__ method for the Vector class of Section 2.3.3, so
# that the expression -v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.

def __neg__(self):
    for i in range(len(self)):
        self[i] = -self[i]
    return self


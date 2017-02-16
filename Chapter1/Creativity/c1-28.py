def norm(v, p = 2):
    import math
    sum = 0             
    for i in v:
        num_expo = i ** p       # list value to the power of p         
        sum += num_expo         # all values are summed
        ans = sum ** (1.0/p)
    return ans

b = [4, 3]
print(norm(b))
b = [1,2,3]
print(norm(b, 3))

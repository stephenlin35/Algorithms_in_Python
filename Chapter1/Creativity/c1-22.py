# Write a short program that takes two arrays a and b of length n storing int values, and returns the product of a and b in array c.

def prod_of_arrays(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] * b[i]
    return c

def prod_of_arrays_v2(a, b):
    c = []
    for i, j in zip(a, b):      # use zip() to iterate over multiple seqs
        c.append(i * j)
    return c    

if __name__ == '__main__':
    print(prod_of_arrays([1,2,3], [1,2,3]))
    print(prod_of_arrays_v2([1,2,3], [1,2,3]))

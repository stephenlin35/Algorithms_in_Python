def prod_of_pair_odd(seq):
    """ Function that takes a sequence of integer values and determines if there is a distinct pair of numbers whose product is odd. """

    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            prod = seq[i] * seq[j]
            if prod & 1 == 1:
                print(seq[i], seq[j])


if __name__ == '__main__':
#    import pdb; pdb.set_trace()
    print(prod_of_pair_odd([1,2,3,4,5,6,7,8,9]))


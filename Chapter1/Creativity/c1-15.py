def distinct_nums(seq):
    
    """ Function that takes a sequence of numbers and determines if all the numbers are different from each other. """
    
    len_seq = len(seq)

    for i in range(len_seq):
        for j in range(i+1, len_seq):
            if seq[i] == seq[j]:
                return False
    return True

if __name__ == '__main__':
    print(distinct_nums([1,2,2]))
    print(distinct_nums([1,2,3]))

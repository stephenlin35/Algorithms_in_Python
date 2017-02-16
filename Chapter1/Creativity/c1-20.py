import random

def produce_shuffle(l):
    
    """ Using only random's randint function to implement random's shuffle function """
    
    list_len = len(l)
    i = 0
    while i < list_len:
        rand_index = random.randint(0, list_len-1)    # get random index
        l[i], l[rand_index] = l[rand_index], l[i]       
        i += 1
    return l

if __name__ == '__main__':
    print(produce_shuffle([1,2,3]))
    print(produce_shuffle([1,2,3]))
    print(produce_shuffle([1,2,3]))

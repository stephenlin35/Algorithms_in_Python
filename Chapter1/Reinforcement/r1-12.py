import random

def rand_choice(seq):
    """ Using only the randrange function to implement the random.choice funtion. """
    seq_len = len(seq)
    rand_index = random.randrange(seq_len)  # get a random index
    return seq[rand_index]                  # return the value at that index

if __name__ == '__main__':
    print(rand_choice('str'))
    print(rand_choice([10,20,30]))


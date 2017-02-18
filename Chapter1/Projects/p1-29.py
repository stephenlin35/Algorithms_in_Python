chars = ['c', 'a', 't', 'd', 'o', 'g']

def recursive_perm(lst): 
    if len(lst) == 1:                       # base case
        return [lst]                        # return list of itself as value
    l = []                                  # list to store result
    for i in range(len(lst)):               # iterate thru list of chars 
        first_letter = lst[i]               # get the first char
        remaining_letters = lst[:i] + lst[i+1:]     # get remaining list chars
        for p in recursive_perm(remaining_letters): # recursively   
            l.append([first_letter] + p)            # get back perm
    return l

def iterative_perm(s):
    stack = list(s)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results
    
#import pdb; pdb.set_trace()
if __name__ == '__main__':
    print('Using recursive function:')
    for i in recursive_perm(chars):
        print(''.join(i))
    
    #import pdb; pdb.set_trace()
    print('Using iterative function')
    s = ''.join(chars)
    for i in iterative_perm(s):
        print(''.join(i))


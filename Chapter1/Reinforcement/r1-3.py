def minmax(data):
    """ Function that takes a sequence of one or more numbers, and returns the smallest and largest numbers in the form of a tuple of length two. """
    
    convert_list = list(data)
    if len(data) < 2:
        return convert_list[0], convert_list[0]
    if convert_list[0] > convert_list[1]:
        max_so_far = convert_list[0]
        min_so_far = convert_list[1]
    else:
        max_so_far = convert_list[1]
        min_so_far = convert_list[0]
    for i in range(2, len(data)):
        if convert_list[i] > max_so_far:
            max_so_far = convert_list[i]
        elif convert_list[i] < min_so_far:
            min_so_far = convert_list[i]
    return min_so_far, max_so_far

if __name__ == '__main__':
    print(minmax([1, 3, 5]))
    print(minmax([4, 5]))
            


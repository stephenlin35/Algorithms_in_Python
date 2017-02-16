def reverse_int_list(int_list):
    rev_list = [0] * len(int_list)
    i = len(int_list) - 1
    j = 0
    while i >= 0:
        rev_list[j] = int_list[i]
        i -= 1
        j += 1
    return rev_list

def reverse_int_list_v2(int_list):
    rev_list = []
    i = 0
    while i < len(int_list):
        rev_list.append(int_list.pop())     # pop mutates original list
    return rev_list


if __name__ == '__main__':
    int_list = [1,2,3]
    print(reverse_int_list(int_list))
    print(reverse_int_list_v2(int_list))
    print(int_list)

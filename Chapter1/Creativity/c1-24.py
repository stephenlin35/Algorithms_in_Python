def count_vowels(s):
    
    """ Function that counds the number of vowels in a given character string """
    
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(count_vowels('banana'))
    print(count_vowels('how are you sir'))
    print(count_vowels('banana how are you sir'))

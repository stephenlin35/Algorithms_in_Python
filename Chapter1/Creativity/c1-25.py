def remove_punct(s):
    
    """ Function that takes a string s, representing a sentence, and returns a copy of the string with all punctuation removed. """

    new_list = []
    for i in s:
        if i.isalnum() or i.isspace():
            new_list.append(i)
    return ''.join(new_list)

if __name__ == '__main__':
    print(remove_punct('i\' just would\'ve'))
    print(remove_punct('banna, and strawberries'))

            

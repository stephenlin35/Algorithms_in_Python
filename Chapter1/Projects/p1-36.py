# Write a Python program that inputs a list of words, separated by
# whitespace, and outputs how many times each word appears in the list. You
# need not worry about efficiency.

str_words = input('Enter a list of string separated by spaces: ')
list_words = str_words.split()
words_dict = {}
for i in set(range(len(list_words))):
    words_dict[list_words[i]] = 0
for i in range(len(list_words)):
    if list_words[i] in words_dict:
        words_dict[list_words[i]] += 1
print(words_dict)

# Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c', ..., 'z'], but without having to type all 26 chars.

alphabet_list = [chr(i) for i in range(97, 123)]
print(alphabet_list)

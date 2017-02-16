# Demonstrate how to use Python's list comprehension syntax to produce the list [0,2,6,12,20,30,42,56,72,90]

produce_list = [i*(i-1) for i in range(1, 11)]
print(produce_list)

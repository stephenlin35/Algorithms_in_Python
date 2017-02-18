# A common punishment for school children is to write out a sentence 
# multiple times. Write a Python stand-alone program that will write out the# following sentence one hundred times: "I will never spam my friends again"# Your program should number each of the sentences and it should make eight # different random-looking typos.

import random

typos = [
            'I\m will never spam my friends again.',
            'I ill never spam my friends again.',
            'I will never spam my friends aign.',
            'I will nerver spam me friends again.',
            'Me will never spam my friend again.',
            'I will never spam my friends again..',
            'I will never spam frien again.',
            'I\'ve never spm friends agin.'
        ]

mistakes = []

punishment = ['I will never spam my friends again.'] * 100

for i in range(8):
    punish_index = random.randint(0, 99)
    while punish_index+1 in mistakes:
        punish_index = random.randint(0,99)
    typo_index = random.randint(0, len(typos)-1)
    punishment[punish_index] = typos[typo_index]
    del typos[typo_index]
    mistakes.append(punish_index+1)

for i in range(100):
    print(str(i+1).ljust(5), punishment[i])
print(mistakes)

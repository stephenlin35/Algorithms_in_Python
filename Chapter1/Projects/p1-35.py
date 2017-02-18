# The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox
# but many people find it surprising. Design a Python program that can test 
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5, 10, 15, 20, ..., 100.

import random

days_in_month = {
                    (2,)                    : 28,
                    (4, 6, 9, 11)           : 30,
                    (1, 3, 5, 7, 8, 10, 12) : 31
                }

n = int(input('Enter the number of people in a room: '))
ppl_bday = []
while n > 0:
    for b in range(n):
        month = random.randint(1, 12)
        m = month
        if month < 10:
            month = '0' + str(month)
        for i in days_in_month.keys():
            if m in i:
                d = days_in_month[i]
                if d < 10:
                    str_d = '0' + str(d)
        day = random.randint(1, d)
        year = random.randint(1900, 2017)
        full_bday = str(month) + '/' + str(day) + '/' + str(year)
        ppl_bday.append(full_bday)
    print(ppl_bday)
    ppl_bday.clear()
    n = int(input('Enter the number of people in a room: '))

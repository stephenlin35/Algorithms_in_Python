# Write a Python that can "make change". Your program should take two numbers as input, one that is a monetary amount
# charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin
#to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or form gov. Try to design it so it reurns as few bills and coins as possible.

def determine_change(charged, given):
    money = { 
            'bills': (1, 5, 10, 20, 50, 100),
            'coins': (1, 5, 10, 25) 
            }
    change = round(given - charged, 2)
    dollar_amt = int(change // 1)
    coin_amt = int(round(change % 1, 2) * 100)
    lst = []
    for rev_index in range(len(money['bills'])-1,-1, -1):
        quo = dollar_amt // money['bills'][rev_index]
        if quo > 0:
            dollar_amt -= money['bills'][rev_index] * quo
            print(quo, 'x', money['bills'][rev_index], 'bill')
#    import pdb; pdb.set_trace()
    for rev_index in range(len(money['coins'])-1, -1, -1):        
        quo = coin_amt // money['coins'][rev_index]
        if quo > 0:
            coin_amt -= money['coins'][rev_index] * quo
            print(quo, 'x', money['coins'][rev_index], 'coin')


if __name__ == '__main__':
    amt_charged = float(input('Enter amount to charge: '))
    amt_given = float(input('Enter amount to be given: '))
    determine_change(amt_charged, amt_given)

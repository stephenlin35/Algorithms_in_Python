# The CreditCard class of Section 2.3 initializes the balance of a new
# account to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The # four-parameter constructor syntax should continue to produce an account
# with zero balance.

class CreditCard:
    def __init__(self, name, bank, acnt, limit, bal = 0):
        self.name = name
        self.bank = bank
        self.acnt = acnt
        self.limit = limit
        self.bal = bal

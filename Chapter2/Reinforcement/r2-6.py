# If the parameter to the make_payment method of the CreditCard class were a# negative number, that would have the effect of raising the balance on the # account. Revise the implementation so that it raises a Value if a negative# value is sent.

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def make_payment(self, amount):
        """ Process customer payment that reduces balance. """
        if amount < 0:
            raise ValueError('Amount must not be negative!')
        self._balance -= amount

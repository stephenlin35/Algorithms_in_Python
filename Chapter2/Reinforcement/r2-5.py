# Use the techniques of Section 1.7 to revise the charge and make_payment
# methods of the CreditCard class to ensure that the caller sends a number as a parameter.

class CreditCard:
    """ A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0374 9387 5305')
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return name of the customer. """
        return self._customer

    def get_bank(self):
        """ Return the bank's name. """

    def get_account(self):
        """ Return the card identifying number (typically stored as a string.) """
        return self._account

    def get_limit(self):
        """ Return current credit limit. """
        return self._limit

    def get_balance(self):
        """ Return current balance. """
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charage was denied.
        """
        try:
            if price + self._balance > self._limit:     # if charge exceeds limit,
                return False                            # cannot accept charge
            else:
                self._balance += price
                return True
        except TypeError as e:
            print('An error has occurred!', e)

    def make_payment(self, amount):
        """ Process customer payment that reduces balance. """
        try:
            self._balance -= amount
        except TypeError as e:
            print('An error has occurred!', e)

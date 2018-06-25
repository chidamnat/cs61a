class Account:
    """An account has a balance and holder information.
    >>> a = Account('John')
    >>> a.deposit(100)
    100
    >>> a.deposit(50)
    150
    >>> a.withdraw(200)
    'Insufficient Funds!'
    """
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds!"
        self.balance -= amount
        return self.balance

class CheckingAccount(Account):
    interest = 0.01
    fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.fee)

class Bank:
    """A bank has accounts

    >>> bank = Bank()
    >>> john = bank.open_account('john',10)
    >>> jack = bank.open_account('jack',5,CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, account_holder,amount, kind=Account):
        account = kind(account_holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1

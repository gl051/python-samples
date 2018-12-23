"""
    Wallet example
"""


class WalletError(Exception):
    pass


class Wallet():
    def __init__(self, amount=0):
        if isinstance(amount, int):
            self._amount = amount
        else:
            raise WalletError

    @property
    def balance(self):
        return self._amount

    def add_cash(self, val):
        self._amount += val

    def get_cash(self, val):
        if val > self.balance:
            raise WalletError
        else:
            self._amount -= val
            return val

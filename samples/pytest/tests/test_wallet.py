import pytest
from util.wallet import Wallet, WalletError


def test_integer_cash_parameter():
    with pytest.raises(WalletError):
        Wallet('aaa')


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet_10():
    ''' Return a wallet with 10$'''
    return Wallet(10)


def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0


def test_no_money(empty_wallet):
    with pytest.raises(WalletError):
        empty_wallet.get_cash(100)


# Testing multiple transaction using fixture and parametrize
@pytest.mark.parametrize("deposit, withdraw", [
    (100, 50),
    (50, 50),
    (45, 5)
])
def test_transaction(empty_wallet, deposit, withdraw):
    assert empty_wallet.balance == 0
    empty_wallet.add_cash(deposit)
    assert empty_wallet.balance == deposit
    empty_wallet.get_cash(withdraw)
    assert empty_wallet.balance == (deposit - withdraw)

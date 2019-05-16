# Tutorial on using pytest

Install _pytest_ module:

`pipenv install pytest`

Collect your test cases in files whose name begins with *test_* or ends with *_test.py*. A good practice is to store all your tests under a specific folder:

```
|__test
     |__test_this.py
     |__test_that.py
```

Examples of how to call pytest:
```
pytest tests/
pytest tests/test_cube.py
pytest -q tests
```

To define fixture data, without having to repeat yourself per each test use something like this:

```
@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()
```

To see all the text fixtures you have defined

`pytest --fixtures`

To provide parameterize invocation of the same test use the function decorator:

```
@pytest.mark.parametrize(param1, param2), [(val1, val2), (val1, val2)]
```

To jump into a PDB session at the first failure of your tests:

`pytest --pdb tests/`

### Running tests
```
pytest tests/test_square.py
pytest tests/test_wallet.py  
```

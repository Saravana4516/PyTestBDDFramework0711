import pytest
from pytest_bdd import scenario


# sample scenario
@pytest.mark.parametrize(['Username', 'Password'], [('', '')])
@scenario('../features/sample.feature', 'Verify the login functionality')
def test_sample01(Username, Password):
    """"""

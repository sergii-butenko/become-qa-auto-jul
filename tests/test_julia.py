import pytest


class User():

    def __init__(self, username, second_name) -> None:
        self.username = username
        self.second_name = second_name


@pytest.fixture(scope='module')
def user():
    print("CREATE USER")
    user = User('Sergii', 'Butenko')
    yield user
    print("REMOVE USER")


@pytest.mark.api
def test_check_username(user):
    assert user.username == 'Sergii'


@pytest.mark.api
def test_check_username2(user):
    assert user.second_name == 'Butenko'

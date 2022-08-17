from providers.data.users_provider import UserProvider
import requests
import pytest


def test_http_status_code200(github_api_client):
    r = requests.get('https://api.github.com/zen')

    assert r.status_code == 200


def test_user_exists(github_api_client):
    user = UserProvider.existing_user()
    user = github_api_client.get_user(user['username'])

    assert user['login'] == user['username']
    assert user['id'] == user['id']


def test_user_non_exists(github_api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user('defunktlaksjdfjasdf')

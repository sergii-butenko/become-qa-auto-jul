
from providers.data.users_provider import UsersProvider


def test_check_login_failed(github_ui_client):
    user = UsersProvider.fake_user()

    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.get_title() == "Sign in to GitHub · GitHub"

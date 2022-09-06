
from providers.data.users_provider import UsersProvider


def test_check_login_failed(github_ui_client):
    user = UsersProvider.fake_user()

    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.login_page.is_login_error() is False


def test_check_login_btn_is_green(github_ui_client):
    login_btn = github_ui_client.login_page.login_btn

    assert login_btn.color == 'green'

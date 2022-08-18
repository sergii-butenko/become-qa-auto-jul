import os


class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            'login': 'kashekfjhkajsdhfkjhsdaf',
            'id': 789216,
            'password': 'fake_password'
        }

    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': 2,
            'password': 'password'
        }

    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ["EXISTING_GITHUB_USER_LOGIN"],
            'id': int(os.environ.get("EXISTING_GITHUB_USER_ID")),
        }

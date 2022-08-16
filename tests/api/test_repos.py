def test_check_repos_can_be_found(github_api_client):
    # Check user can find any existing repo from github
    repos = github_api_client.get_repos('become-qa-auto')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0


def test_check_repos_cannot_be_found(github_api_client):
    # Check user can find any existing repo from github
    repos = github_api_client.get_repos('kajshdkjfhaksjhdfkjhasdkfjhaskdfh')

    assert repos['total_count'] == 0
    assert len(repos['items']) == 0

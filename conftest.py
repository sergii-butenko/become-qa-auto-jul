import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from applications.api.github_api import GitHubAPI
from applications.ui.github_ui import GitHubUI
from config.config import Config


@pytest.fixture(scope="session")
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url_api, "v1")

    yield github_api_client

    print("END-UP TEST")


@pytest.fixture()
def github_ui_client():
    driver = webdriver.Chrome(
        service=Service(r"/home/sbutenko/repos/LnD/become-qa-auto-jul/chromedriver")
    )

    github_ui_client = GitHubUI(Config.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()

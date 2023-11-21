import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="russian",
                     help="Choose language: russian or english")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("language")

    options.add_experimental_option(
        'prefs', {'intl.accept_languages': "language"})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_2(request):
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

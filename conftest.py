import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, ...(etc.)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is not None:
        print("\nstart chrome browser for test..")
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options_chrome,)
    else:
        raise pytest.UsageError("--langauge should be ru, en, ...(etc.)")

    
    
    yield browser
    print("\nquit browser..")
    browser.quit()

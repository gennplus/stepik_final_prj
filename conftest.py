import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = ChromeOptions()
        options_chrome.add_argument('--headless')
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.headless = True
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# This is a registered hook in pytest
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose your language")

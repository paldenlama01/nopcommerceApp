import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    yield driver



def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the Browser value to setup method
    return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # Check if metadata exists (to avoid errors if plugin isn't installed)
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Palden'

# It is hook for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None) # Note: Usually uppercase in Windows
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
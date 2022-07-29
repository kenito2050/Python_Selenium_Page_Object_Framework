import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="LA",
                     help="Environment to run test against")
    parser.addoption("--browser", action="store", default="CHROME",
                     help="Browser to run test against")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")





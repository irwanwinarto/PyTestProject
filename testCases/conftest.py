from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()  # might need to specify file path
    return driver

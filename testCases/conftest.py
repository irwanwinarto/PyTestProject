from selenium import webdriver
import pytest
import time


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()  # might need to specify file path
    # driver.get("https://www.google.com")
    # time.sleep(5)
    return driver

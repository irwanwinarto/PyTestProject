import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from pageObjects.loginPage import LoginPage


class TestLogin1:
    baseURL = "https://www.nopcommerce.com/en/demo"
    username = "admin@yourstore.com"
    password = "admin"
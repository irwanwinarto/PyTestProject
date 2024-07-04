from webbrowser import get

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.loginPage import LoginPage



class TestLogin1:
    baseURL = "https://www.nopcommerce.com/en/demo"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage(self, setup):
        self.driver = setup
        self.driver = get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False, "Failed to access home page."

    def test_login(self, setup):
        self.driver = setup
        self.driver = get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        actual_title = self.driver.title
        if actual_title == "Dashboard /poCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            self.driver.close()
            assert False, "Failed to log in."

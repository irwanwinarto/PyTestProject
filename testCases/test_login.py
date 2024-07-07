import webbrowser
from webbrowser import get

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.loginPage import LoginPage
import requests


class TestLogin1:
    baseURL = "https://www.nopcommerce.com/en/demo"
    username = "admin@yourstore.com"    # dummy values. Use a secrets manager.
    password = "admin"  # dummy values. Use a secrets manager.

    @pytest.mark.sanity
    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title  # this is a selenium method. It does not take in any arguments. Just grabs the page title. neat.

        if actual_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False, "Failed to access home page."

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)  # hits the constructor
        self.lp.set_username(self.username)  # type in the username
        self.lp.set_password(self.password)  #types in the password
        self.lp.click_login()

        actual_title = self.driver.title
        if actual_title == "Dashboard /poCommerce administration": # we can get more information by Inspecting the webpage
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            self.driver.close()
            assert False, "Failed to log in."

    @pytest.mark.testthis
    def test_one(self, setup):
        self.driver = setup
        print("This works")
        self.driver.get(self.baseURL)

    @pytest.mark.pokeapi
    def test_pokeapi(self, setup):
        print("\nHELLO WORLD\n")
        url = "https://pokeapi.co/api/v2/pokemon/charmander"
        response = requests.get(url)
        print(f"\nRESPONSE: {response.content}\n")
        # Verify status code
        assert response.status_code == 200

    @pytest.mark.apitest
    def test_get_book_by_id(self):
        url = "https://run.mocky.io/v3/01123071-8b34-41af-b787-f666fad3ca33"  # Replace with your mock API URL
        response = requests.get(url)
        print("\nRESPONSE: {} \n".format(response.content))

        # Verify status code
        assert response.status_code == 200

import webbrowser
from webbrowser import get

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.loginPage import LoginPage
import requests


class TestPokeAPI:
    @pytest.mark.pokeapi
    def test_get_pokemon_details(self):
        pokemon = 'charmander'
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        resp = response.json()
        print("\nRESPONSE: {} \n".format(resp['name']))
        # Verify status code
        assert response.status_code == 200


    @pytest.mark.pokeapi2
    def test_get_berry_details(self):
        berry_name = 'gojiberry'
        url = f"https://pokeapi.co/api/v2/berry/{berry_name}"
        response = requests.get(url)
        assert response.status_code == 200



    @pytest.mark.mockytest
    def test_get_book_by_id(self):
        url = "https://run.mocky.io/v3/01123071-8b34-41af-b787-f666fad3ca33"  # Replace with your mock API URL
        response = requests.get(url)
        print("\nRESPONSE: {} \n".format(response.content))
        # Verify status code
        assert response.status_code == 200
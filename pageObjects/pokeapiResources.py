import pytest
import pokeapiAPI



class PokemonResources:
    pokemon = ""

    def __init__(self, driver): #this is the constructor of this class!
        self.driver = driver    # assign the browser driver.

    def get_pokemon_stat(self, pokemon):
        resp = pokeapiAPI.get_pokemon_details(pokemon)
        # validate name
        assert resp['name'] == pokemon
        return resp

    def get_berry(self, berry):
        # check for berry name or ID only
        resp = pokeapiAPI.get_berry_details(berry)
        return resp

import pytest
import requests


def get_pokemon_details(pokemon, status=200):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    # Verify status code
    assert response.status_code == status
    resp = response.json()
    return resp


def get_berry_details(berry, status=200):
    url = f"https://pokeapi.co/api/v2/berry/{berry}"
    response = requests.get(url)
    assert response.status_code == status
    resp = response.json()
    return resp


def get_berry_firmness_by_id(berry_id, status=200):
    # can use either berry name or berry ID
    url = f"https://pokeapi.co/api/v2/berry-firmness/{berry_id}/"
    response = requests.get(url)
    assert response.status_code == status
    resp = response.json()
    return resp


def get_berry_flavors(berry, status=200):
    # can use either berry name or berry ID
    url = f"https://pokeapi.co/api/v2/berry-flavor/{berry}/"
    response = requests.get(url)
    assert response.status_code == status
    resp = response.json()
    return resp

def get_contest_types(contest, status=200):
    # can use either contest name or contest ID
    url = f"https://pokeapi.co/api/v2/contest-type/{contest}/"
    response = requests.get(url)
    assert response.status_code == status
    resp = response.json()
    return resp

def get_evolution_chain(pokemon_id, status=200):
    url = f"https://pokeapi.co/api/v2/evolution-chain/{pokemon_id}/"
    response = requests.get(url)
    assert response.status_code == status
    resp = response.json()
    return resp

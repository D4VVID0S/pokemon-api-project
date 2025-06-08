# Provides a function to retrieve all Pokémon entries
# (name and URL) from the PokéAPI, handling pagination.

import os
import requests
from dotenv import load_dotenv
import time

API_BASE_URL = f"https://pokeapi.co/api/v2/pokemon/"
# Maximum number of pokemon to fetch detailed data for (0 = no limit)
MAX_POKEMONS = int(os.getenv("MAX_POKEMONS", "10"))

def get_all_pokemons():
    """
    Retrieve all Pokémon entries (name and URL) from the PokéAPI.

    This function iterates through all paginated results, collecting
    each page's 'results' list until there are no more pages.

    Returns:
        A list of dictionaries for each Pokémon, containing:
        'id' (int)
        'name' (str)
        'height' (int)
        'weight' (int)
        'abilities' (list of str)
        'sprites' (dict)
        'stats' (list of {'stat': str, 'base_stat': int})
        'types' (list of str)
    
    References:
        - PokéAPI Pokémon endpoint: https://pokeapi.co/docs/v2#pokemon
        - requests documentation: https://docs.python-requests.org/
    """

    pokemons = []
    next_url = f"{API_BASE_URL}"

    while next_url:
        # Send GET request to the current page URL
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

        # Append this page's results
        pokemons.extend(data.get('results', []))

        # Update next_url to the 'next' page URL, or None if done
        next_url = data.get('next')

        # Fetch full details for each Pokemon
        detailed_pokemons = []
        # Apply testing limit if set
        for entry in (pokemons[:MAX_POKEMONS] if MAX_POKEMONS > 0 else pokemons):
            resp = requests.get(entry['url'])
            resp.raise_for_status()
            data = resp.json()
            detailed_pokemons.append({
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "abilities": [ability_entry["ability"]["name"] for ability_entry in data["abilities"]],
                "sprites": data["sprites"],
                "stats": [
                    {"stat": stat_entry["stat"]["name"], "base_stat": stat_entry["base_stat"]}
                    for stat_entry in data["stats"]
                ],
                "types": [type_entry["type"]["name"] for type_entry in data["types"]],
            })
            time.sleep(0.1)
        return detailed_pokemons
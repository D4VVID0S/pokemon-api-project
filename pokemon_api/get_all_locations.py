"""
Provides a function to retrieve all Locations that can be visited within the games
- 'id' (integer)
- 'name' (string)
- 'region' (string)
- 'game_indices' (list)
- 'areas' (list)
"""

import os
import requests
from dotenv import load_dotenv
import time

API_BASE_URL = f"https://pokeapi.co/api/v2/location/"
MAX_LOCATIONS = int(os.getenv("MAX_LOCATIONS", "0"))

def get_all_locations():
    """
    This function iterates through all paginated results, collecting
    each page's 'results' list until there are no more pages.

    Returns:
        A list of detailed location dictionaries, each containing:
        'id' (integer)
        'name' (string)
        'region' (dict with 'name' and 'url')
        'names' (list of dicts with 'name' and 'language')
        'game_indices' (list of dicts with 'game_index' and 'language')
        'areas' (list of dicts with 'name' and 'url')
    
    References:
    - PokéAPI Pokémon endpoint: https://pokeapi.co/docs/v2#locations-section
    - requests documentation: https://docs.python-requests.org/
    """

    locations = []
    next_url = f"{API_BASE_URL}"

    while next_url:
        # Send GET request to the current page URL
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

        # Append this page's results
        locations.extend(data.get('results', []))

        # Update next_url to the 'next' page URL, or None if done
        next_url = data.get('next')

    # Fetch full details for each Location after collecting all entries
    detailed_locations = []
    
    # Apply testing limit if set
    for entry in (locations[:MAX_LOCATIONS] if MAX_LOCATIONS > 0 else locations):
        resp = requests.get(entry['url'])
        resp.raise_for_status()
        data = resp.json()
        detailed_locations.append({
            "id": data["id"],
            "name": data["name"],
            "region": {
                "name": data["region"]["name"],
                "url": data["region"]["url"]
            },
            "names": [
                {
                    "name": name_entry["name"],
                    "language": {
                        "name": name_entry["language"]["name"],
                        "url": name_entry["language"]["url"]
                }
            }
            for name_entry in data["names"]
            ],
            "game_indices": [
                {
                    "game_index": game_index_entry["game_index"],
                    "generation": {
                        "name": game_index_entry["generation"]["name"],
                        "url": game_index_entry["generation"]["url"]
                    }
                }
                for game_index_entry in data["game_indices"]
            ],
            "areas": [
                {
                    "name": areas_entry["name"],
                    "url": areas_entry["url"]
                }
                for areas_entry in data["areas"]
            ],
        })
        time.sleep(0.1)
        
    return detailed_locations
from pokemon_api.get_all_pokemons import get_all_pokemons
import polars as pl

def load_pokemons_dataframe():
    # Fetch all Pokemon entries from the PokeAPI and return as a Polars DataFrame

    # Returns:
    #   pl.DataFrame: with columns 'name' and 'url'
    
    # Call the function to get a list of dicts
    pokemons = get_all_pokemons()

    df = pl.DataFrame(pokemons)

    return df

### Entry point for the Python Pokédex application.

## Imports
import polars as pl
## DataFrame manipulation
from store_data.create_csv import create_csv
## Pokemons
from store_data.pokemons.pokemons_dataframe import load_pokemons_to_dataframe
from store_data.pokemons.pokemons_dataframe import edit_stats_to_basic_uom
## Locations
from store_data.locations.locations_dataframe import load_locations_to_dataframe

def main():
    """
    1. Loads all Pokémon into a DataFrame and displays a summary.
    2. Adds columns with converted UoMs for height (m) and weight(kg)
    3. Creates a .csv file with the fetched data
    """
    # set display precision to 2 decimals for all Float32/Float64
    pl.Config.set_float_precision(2)
    
    pokemon_df = load_pokemons_to_dataframe()
    pokemon_df = edit_stats_to_basic_uom(pokemon_df)
    pokemon_df = create_csv(pokemon_df)
    
    print(f"Total Pokémon fetched: {len(pokemon_df)}")
    print(pokemon_df.head(10))

    # create_csv(pokemon_df)

    # """
    # 1. Loads all Locations into a DataFrame and displays a summary.
    # 2. Creates a .csv file with the fetched data
    # """

    # locations_df = load_locations_to_dataframe()
    # print(f"Total Locations fetched: {len(locations_df)}")
    # print(locations_df.head(10))
    # create_csv(locations_df)

if __name__ == "__main__":
    main()

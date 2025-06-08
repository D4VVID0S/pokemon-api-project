from pokemon_api.get_all_pokemons import get_all_pokemons
import polars as pl

def load_pokemons_to_dataframe():
    # Fetch all Pokemon entries from the PokeAPI and return as a Polars DataFrame

    # Returns:
    #   pl.DataFrame: with columns 'name' and 'url'
    
    # Call the function to get a list of dicts
    pokemons = get_all_pokemons()

    df = pl.DataFrame(pokemons)

    return df

def edit_stats_to_basic_uom(df):
    """
    Convert the 'height; and 'weight' columns to basic UOM for the given DataFrame.
    
    Parameters:
        df (pl.DataFrame): DataFrame containing 'height' column in decimeters and 'weight' column in hectograms.

    Returns:
        pl.DataFrame: New DataFrame with additional columns:
            - "height_m" (float): height converted to meters.
            - 'weight_kg' (float): weight converted to kilograms.
    """

    return df.with_columns([
        (pl.col("height") / 10)
        .round(2)
        .alias("height_m"),
        (pl.col("weight") / 10)
        .round(2)
        .alias("weight_kg")
    ])
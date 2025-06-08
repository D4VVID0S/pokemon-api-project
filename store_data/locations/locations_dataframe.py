from pokemon_api.get_all_locations import get_all_locations
import polars as pl

def load_locations_to_dataframe() -> pl.DataFrame:
    """
    Fetch all Location entries from the PokeAPI and return as a Polars DataFrame
    
    
    Returns:
        pl.DataFrame: DataFrame containing all locations with their nested details.
    """
    # Call the function to get a list of dicts
    locations = get_all_locations()

    df = pl.DataFrame(locations)

    return df
#!/usr/bin/env python3
"""
main.py

Entry point for the Python Pokédex application.
"""

from store_data.pokemons_dataframe import load_pokemons_to_dataframe
from store_data.pokemons_dataframe import edit_stats_to_basic_uom
import polars as pl


def main():
    """
    Loads all Pokémon into a DataFrame and displays a summary.
    """
    # set display precision to 2 decimals for all Float32/Float64
    pl.Config.set_float_precision(2)
    
    df = load_pokemons_to_dataframe()
    df = edit_stats_to_basic_uom(df)
    print(f"Total Pokémon fetched: {len(df)}")
    print(df.head(10))


if __name__ == "__main__":
    main()
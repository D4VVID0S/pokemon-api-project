#!/usr/bin/env python3
"""
main.py

Entry point for the Python Pokédex application.
"""

from store_data.pokemons_dataframe import load_pokemons_dataframe


def main():
    """
    Loads all Pokémon into a DataFrame and displays a summary.
    """
    df = load_pokemons_dataframe()
    print(f"Total Pokémon fetched: {len(df)}")
    print(df.head(10))


if __name__ == "__main__":
    main()
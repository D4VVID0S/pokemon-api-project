

# Python Pokédex

A simple command-line Pokédex built in Python using the [PokéAPI](https://pokeapi.co/docs/v2).

## Features

- Fetch Pokémon data via REST API using `requests`
- Modular codebase: each component lives in its own module

## Prerequisites

- Python 3.7+ ([Python docs](https://docs.python.org/3/))
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/d4vvid0s/pokemon-api-project.git
   cd pokemon-api-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage (not working yet)

Fetch and display data from the Pokémon games:
```bash
pokedex get pikachu
```

## Future Improvements

- Analyze and tabulate data with [polars](https://pola-rs.github.io/polars/py-polars/html/) or [pandas](https://pandas.pydata.org/docs/)
- GUI with [PySimpleGUI](https://pysimplegui.readthedocs.io/) or [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Add commands: search by type, ability, evolution chains, etc.

## References

- [PokéAPI Documentation](https://pokeapi.co/docs/v2)
- [requests Documentation](https://requests.readthedocs.io/)
- [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [requests-cache Documentation](https://requests-cache.readthedocs.io/)
- [rich Documentation](https://rich.readthedocs.io/)
- [click Documentation](https://click.palletsprojects.com/)
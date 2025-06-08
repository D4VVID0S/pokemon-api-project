

# Python Pokédex

A simple command-line Pokédex built in Python using the [PokéAPI](https://pokeapi.co/docs/v2).

## Features

- Fetch Pokémon data via REST API using `requests`
- Model responses with `pydantic` or `dataclasses` ([Python docs](https://docs.python.org/3/library/dataclasses.html))
- Cache API requests with `requests-cache`
- Pretty-print output with `rich`
- CLI interface powered by `click`
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

## Project Structure

```
pokemon-api-project/
├── pokedex/
│   ├── __init__.py
│   ├── api.py          # HTTP functions for PokéAPI
│   ├── models.py       # Data models with pydantic/dataclasses
│   ├── cache.py        # requests-cache setup
│   └── cli.py          # click-based CLI commands
├── tests/
│   └── test_models.py  # pytest tests
├── .env                # environment variables (ignored by git)
├── .gitignore
├── requirements.txt
└── readme.md
```

## Usage

Fetch and display a Pokémon:
```bash
pokedex get pikachu
```

## Configuration

Create a `.env` file to override defaults:
```
API_BASE_URL=https://pokeapi.co/api/v2
CACHE_EXPIRE=3600
```

## Future Improvements

- Analyze and tabulate data with [polars](https://pola-rs.github.io/polars/py-polars/html/) or [pandas](https://pandas.pydata.org/docs/)
- GUI with [PySimpleGUI](https://pysimplegui.readthedocs.io/) or [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Package and publish with [poetry](https://python-poetry.org/)
- Add commands: search by type, ability, evolution chains, etc.

## References

- [PokéAPI Documentation](https://pokeapi.co/docs/v2)
- [requests Documentation](https://requests.readthedocs.io/)
- [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [requests-cache Documentation](https://requests-cache.readthedocs.io/)
- [rich Documentation](https://rich.readthedocs.io/)
- [click Documentation](https://click.palletsprojects.com/)
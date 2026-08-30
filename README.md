# FinTrack

A lightweight personal finance tracker built with Python and SQLite.

## Disclaimer

FinTrack is a personal software project intended for educational and informational purposes. It is not financial, tax, accounting, or investment advice.

## Current Features

* SQLite database for persistent transaction storage
* Add financial transactions
* View stored transactions
* Update existing transactions
* Delete transactions
* Transaction IDs
* Transaction categories and descriptions
* Strict `MM-DD-YYYY` date validation
* Amount validation
* Transaction ID validation
* Handling for nonexistent transaction IDs
* Looping command-line interface
* `fintrack` command for launching the application
* Git-based version control

## Tech Stack

* **Python** — Programming language
* **SQLite** — Database engine
* **Git** — Version control
* **GitHub** — Repository hosting
* **Visual Studio Code** — Development environment
* **Black Formatter** — Code formatting

## Project Structure

```text
FinTrack/
├── data/
│   └── fintrack.db
├── fintrack/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── transactions.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Installation

Clone the repository and create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Install FinTrack in editable mode:

```powershell
python -m pip install -e .
```

## Running FinTrack

After installation, launch FinTrack with:

```powershell
fintrack
```

Alternatively, it can be launched directly as a Python module:

```powershell
python -m fintrack.main
```

The application initializes the SQLite database and displays the main menu:

```text
1. Add
2. View
3. Update
4. Delete
5. Exit
Choose:
```

## Date Format

Transaction dates must use:

```text
MM-DD-YYYY
```

Example:

```text
08-30-2026
```

FinTrack validates dates before allowing a transaction to be created or updated.

## Roadmap

* [ ] Improve transaction input validation
* [ ] Add transaction filtering
* [ ] Add transaction searching
* [ ] Add income and expense summaries
* [ ] Add budgeting
* [ ] Add financial reports
* [ ] Add charts and data visualization
* [ ] Improve error handling
* [ ] Add automated tests
* [ ] Build a graphical user interface
* [ ] Prepare FinTrack for distribution

## Development Environment

**Hardware:** Microsoft Surface Go 2

**Operating System:** Windows 11

**Development Environment:** Visual Studio Code

## AI Acknowledgments

FinTrack was developed independently with minor assistance from **ChatGPT** for programming guidance, debugging assistance, and explanations of Python, SQLite, Git, and related development concepts.

All application code, project structure, design decisions, and implementation were developed as part of the FinTrack project.

## License

FinTrack is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

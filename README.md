# FinTrack

A lightweight personal finance tracker built with Python and SQLite.

## Disclaimer

FinTrack is a personal software project intended for educational and informational purposes. It is not financial, tax, accounting, or investment advice.

## Current Features

* SQLite database for persistent transaction storage
* Add financial transactions
* View stored transactions
* View transactions by type
* View transactions by category
* Update transactions
* Delete transactions
* Transaction categories and descriptions
* Strict `MM-DD-YYYY` date validation
* Positive amount validation
* Required-field input validation
* Transaction ID validation
* Reusable transaction display helper
* Git-based version control
* `fintrack` command for launching the application

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
│   ├── database.py
│   ├── main.py
│   └── transactions.py
├── .gitignore
├── README.md
├── pyproject.toml
└── .venv/
```

## Running FinTrack

After activating the virtual environment, FinTrack can be launched with:

```powershell
fintrack
```

The application initializes the database and displays the main menu.

Alternatively, it can be run with:

```powershell
python -m fintrack.main
```

### Date Format

Dates must use:

```text
MM-DD-YYYY
```

Example:

```text
08-30-2026
```

### View Menu

The View menu currently supports:

```text
1. View All
2. View by ID (TBA)
3. View by Date (TBA)
4. View by Type
5. View by Category
6. Back
```

## Roadmap

* [ ] Add transaction filtering by ID
* [ ] Add transaction filtering by date
* [ ] Add income and expense summaries
* [ ] Add budgeting
* [ ] Add financial reports
* [ ] Build a graphical user interface
* [ ] Add charts and data visualization
* [ ] Improve error handling
* [ ] Add automated tests

## Development Environment

**Hardware:** Microsoft Surface Go 2

**Operating System:** Windows 11

**Development Environment:** Visual Studio Code

## AI Acknowledgments

FinTrack was developed independently with minor assistance from **ChatGPT** (Free Plan) for programming guidance, debugging assistance, and writing Git commits.

All application code, project structure, design decisions, and implementation were developed as part of the FinTrack project.

## License

FinTrack is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.
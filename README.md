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
* Numeric amount validation
* Positive transaction amount validation
* Required-field validation
* Invalid input retry handling
* Transaction ID validation
* Handling for nonexistent transaction IDs
* Looping command-line interface
* Installable `fintrack` command
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
│   ├── database.py
│   ├── main.py
│   └── transactions.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── .venv/
```

## Running FinTrack

After installing FinTrack as an editable package:

```powershell
python -m pip install -e .
```

FinTrack can be launched with:

```powershell
fintrack
```

The application will initialize the database and display the main menu.

The module-based command is also available:

```powershell
python -m fintrack.main
```

## Main Menu

```text
1. Add
2. View
3. Update
4. Delete
5. Exit
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

### Input Validation

FinTrack currently validates:

* Dates
* Transaction amounts
* Positive transaction amounts
* Transaction IDs
* Required text fields
* Menu selections

Invalid input is rejected and the user is prompted again instead of the application terminating.

## Roadmap

* [ ] Add transaction filtering
* [ ] Add transaction searching
* [ ] Add income and expense summaries
* [ ] Add budgeting
* [ ] Add financial reports
* [ ] Add charts and data visualization
* [ ] Improve database error handling
* [ ] Add automated tests
* [ ] Build a graphical user interface
* [ ] Prepare FinTrack for distribution

## Development Environment

**Hardware:** Microsoft Surface Go 2

**Operating System:** Windows 11

**Development Environment:** Visual Studio Code

## AI Acknowledgments

FinTrack was developed independently with minor assistance from **ChatGPT** (Free Plan) for programming guidance, debugging assistance, explanations of Python, SQLite, and Git concepts, and README assistance.

All application code, project structure, design decisions, and implementation were developed as part of the FinTrack project.

## License

FinTrack is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

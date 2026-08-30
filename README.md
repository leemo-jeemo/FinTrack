# FinTrack

A lightweight personal finance tracker built with Python and SQLite.

## Disclaimer
FinTrack is a personal software project intended for educational and informational purposes. It is not financial, tax, accounting, or investment advice.

## Current Features

* SQLite database for persistent transaction storage
* Add financial transactions
* View stored transactions
* Transaction categories and descriptions
* Strict `MM-DD-YYYY` date validation
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
├── README.md
└── .venv/
```

## Running FinTrack

Activate the virtual environment, then run:

```powershell
python -m fintrack.main
```

The application will initialize the database and prompt you for a transaction.

### Date Format

Dates must use:

```text
MM-DD-YYYY
```

Example:

```text
08-30-2026
```

## Roadmap

* [ ] Improve transaction input validation
* [ ] Add transaction editing
* [ ] Add transaction deletion
* [ ] Add transaction filtering
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

FinTrack was developed independently with minor assistance from **ChatGPT** (Free Plan) for programming guidance, debugging assistance, and explanations of Python, SQLite, and Git concepts (and making my README.md).

All application code, project structure, design decisions, and implementation were developed as part of the FinTrack project.

## License

FinTrack is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

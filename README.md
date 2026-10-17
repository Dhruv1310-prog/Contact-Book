# Contact Book

A command-line contact management application built with Python. This project allows users to store, view, search, update, and delete contacts through a simple text-based interface.

## Features

- Add and view contacts
- Search for contacts
- Update contact details
- Delete contacts
- Validate phone numbers and email addresses
- Store contact data in JSON for persistence
- Run the application using a Windows batch file

## Project Structure

```text
Contact-Book/
├── contact.py
├── contact_book.py
├── main.py
├── contacts.json
├── run.bat
├── README.md
└── .gitignore
```

- `contact.py` — represents an individual contact.
- `contact_book.py` — manages the collection of contacts and data storage.
- `main.py` — provides the command-line user interface.
- `run.bat` — launches the application on Windows.
- `contacts.json` — stores contact data locally and is excluded from Git tracking.

## Requirements

- Python 3 installed
- Windows operating system to use the batch launcher

## How to Run

1. Clone or download this repository.
2. Make sure Python is installed and available from the command line.
3. Run `run.bat` to launch the application.

Alternatively, open a terminal in the project folder and run:

```bash
python main.py
```

## Data Storage

Contacts are stored locally in JSON format so that they can be loaded again when the application is reopened. The local data file is excluded from version control to avoid uploading personal contact information.

## Learning Outcomes

This project helped me practise:

- Python classes and objects
- Modular programming and imports
- Lists and dictionaries
- Functions and input validation
- Exception handling
- JSON file handling
- Git and GitHub version control

## Future Improvements

- Improve input validation and error handling
- Add automated tests
- Improve contact search and duplicate detection
- Add support for exporting and importing contacts

---

**Note:** This is a learning project, and its features may evolve as I continue improving it.

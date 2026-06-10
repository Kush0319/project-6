# Personal Journal Manager (File Operator)

A command-line based Python application that allows users to maintain a personal journal. This project demonstrates strong foundational Python skills, focusing on Object-Oriented Programming (OOP), file I/O operations, and exception handling without the use of any external imported libraries.

## 📝 Overview

The Personal Journal Manager provides a simple, menu-driven interface for users to add, view, search, and delete journal entries. All entries are stored locally in a text file (`journal.txt`), ensuring that data persists between sessions. 

## ✨ Features

- **Add a New Entry:** Users can write new journal entries. The program appends the entry to the journal file, creating the file automatically if it doesn't exist.
- **View All Entries:** Displays all previously saved journal entries directly in the console. Handles cases where the file might not exist yet.
- **Search for an Entry:** Allows users to search through their journal using specific keywords or dates to easily find past entries.
- **Delete All Entries:** Clears the entire journal with a built-in user confirmation prompt to prevent accidental data loss.
- **Graceful Error Handling:** Program will not crash on unexpected inputs, missing files, or permission errors.

## 🎯 Learning Objectives Demonstrated

- **File Handling:** Implementation of read (`r`), write (`w`), and append (`a`) modes.
- **Exception Handling:** Managing potential runtime errors like `FileNotFoundError` and `PermissionError` using `try-except` blocks.
- **Object-Oriented Programming (OOP):** Structuring the application using classes (`JournalManager`), methods, and encapsulation.
- **Control Flow:** Using Python 3.10+ `match...case` syntax for clean menu navigation.

## 🚀 Prerequisites

- **Python 3.10 or higher** (Required because the code utilizes the `match...case` statement introduced in Python 3.10).
- No additional modules or libraries are required (100% Core Python).

## 💻 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone <your-github-repo-link-here>

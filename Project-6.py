class JournalManager:
    """
    A class to manage personal journal entries using manual file handling.
    """
    def __init__(self):
        self.filename = "journal.txt"
    def add_entry(self):
        """Appends a new journal entry with a user-provided timestamp."""
        timestamp = input("\nEnter current date/time (e.g., 19-02-2005 10:00:00): ")
        entry_text = input("Enter your journal entry:\n")
        try:
            file = open(self.filename, 'a')
            file.write(f"[{timestamp}]\n")
            file.write(f"{entry_text}\n\n")
            file.close() 
            print("\nEntry added successfully!")   
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_entries(self):
        """Reads and displays all entries from the journal file."""
        try:
            file = open(self.filename, 'r')
            content = file.read()
            file.close()
            if content.strip():
                print("\nYour Journal Entries:")
                print("---------------------------")
                print(content.strip())
            else:
                print("\nNo journal entries found. Start by adding a new entry!")            
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def search_entry(self):
        """Searches for a specific keyword in the journal file."""
        keyword = input("\nEnter a keyword or date to search: ")
        try:
            file = open(self.filename, 'r')
            raw_content = file.read().strip()
            file.close() 
            entries = raw_content.split('\n\n')
            found_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    found_entries.append(entry)
            if found_entries:
                print("\nMatching Entries:")
                print("---------------------------")
                for match in found_entries:
                    print(match + "\n")
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")       
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except Exception as e:
             print(f"\nAn unexpected error occurred: {e}")

    def delete_entries(self):
        """Clears the entire journal file after prompting the user."""
        try:
            file = open(self.filename, 'r')
            file.close()      
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").lower()
            if confirm == 'yes':
                file = open(self.filename, 'w')
                file.close()
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDeletion cancelled.")  
        except FileNotFoundError:
            print("\nNo journal entries to delete.")
        except PermissionError:
            print("\nError: The file is currently in use or you lack permissions to delete it.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

journal = JournalManager()

while True:
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    
    choice = input("\nUser Input:")
    match choice:
        case '1':
            journal.add_entry()
        case '2':
            journal.view_entries()
        case '3':
            journal.search_entry()
        case '4':
            journal.delete_entries()
        case '5':
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please select a valid option from the menu.")
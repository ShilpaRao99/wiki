import os
import re

# Path where encyclopedia entries are stored
ENTRIES_DIR = "entries"

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    files = os.listdir(ENTRIES_DIR)
    return list(sorted(re.sub(r"\.md$", "", file) for file in files if file.endswith(".md")))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. Returns None if no such entry exists.
    """
    try:
        with open(f"{ENTRIES_DIR}/{title}.md", "r") as file:
            return file.read()
    except FileNotFoundError:
        return None

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown content. If an entry with the same title already exists, it is replaced.
    """
    with open(f"{ENTRIES_DIR}/{title}.md", "w") as file:
        file.write(content)

# List all entries
print("Listing entries:")
print(list_entries())  # Should return all entry names without '.md' extensions

# Test retrieval with a sample title
title = "SampleEntry"  # Replace with the actual title of an entry in entries folder
print(f"\nGetting entry for '{title}':")
print(get_entry(title))  # Should return the content if the entry exists

# Save a new entry
new_title = "NewEntry"
new_content = "# New Entry\nThis is a new entry."
save_entry(new_title, new_content)
print(f"\nNew entry '{new_title}' saved. Checking list:")
print(list_entries())  # New entry should appear in the list

# Retrieve the new entry to verify
print(f"\nContent of '{new_title}':")
print(get_entry(new_title))  # Should match `new_content`

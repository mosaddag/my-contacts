"""
My Contacts
CS50 Final Project
------------------

Author: Mosaddag Awad
Description:
    A simple command-line contact manager built with Python.
    The program allows users to:
      - Add new contacts (name and phone number)
      - View all saved contacts
      - Search for a contact by name
      - Delete a contact
      - Exit the program

    All data is stored in a local CSV file (contacts.csv)
    so that contacts remain saved even after the program exits.

Technologies Used:
    - Python 3
    - CSV File Handling
    - Basic Input/Output
    - Control Structures (if/else, loops, functions)

How to Run:
    1. Open the terminal in the project folder.
    2. Run the command: python3 contacts.py
    3. Follow the on-screen menu options.

CS50 Requirements:
    This project demonstrates file handling, user input, and logic flow —
    covering the fundamentals required for the final project.
"""

import csv
import os

FILENAME = "contacts.csv"

# Ensure the CSV file exists and has a header
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone"])


def add_contact():
    """Add a new contact to the CSV file."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    with open(FILENAME, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])

    print(f"\n✅ Contact '{name}' added successfully!\n")


def view_contacts():
    """Display all saved contacts."""
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        contacts = list(reader)

        if not contacts:
            print("\n⚠️ No contacts found.\n")
            return

        print("\n📋 All Contacts:")
        print("-" * 30)
        for i, (name, phone) in enumerate(contacts, start=1):
            print(f"{i}. {name} - {phone}")
        print()


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row and row[0].strip().lower() == name:
                print(f"\n🔍 Found: {row[0]} - {row[1]}\n")
                found = True
                break

    if not found:
        print(f"\n❌ No contact found with name '{name}'.\n")


def delete_contact():
    """Delete a contact by name."""
    name_to_delete = input("Enter the name of the contact to delete: ").strip().lower()
    updated_contacts = []
    deleted = False

    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row and row[0].strip().lower() != name_to_delete:
                updated_contacts.append(row)
            else:
                deleted = True

    with open(FILENAME, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(updated_contacts)

    if deleted:
        print(f"\n🗑️ Contact '{name_to_delete}' has been deleted.\n")
    else:
        print(f"\n❌ No contact found with name '{name_to_delete}'.\n")


def main():
    """Main program loop."""
    while True:
        print("=== My Contacts ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid option, please try again.\n")


if __name__ == "__main__":
    main()

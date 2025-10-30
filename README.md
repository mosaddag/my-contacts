# My Contacts

#### Video Demo: https://youtu.be/k_U24Nw-yow
#### Description:

**My Contacts** is a simple contact management program built in Python for my CS50 Final Project.  
It allows users to **add, view, search, and delete** contacts, storing all data in a CSV file.

### Features
- Add new contact (name + phone number)
- View all contacts
- Search for a contact by name
- Delete an existing contact
- Data is stored permanently in `contacts.csv`

### How It Works
When the program starts, a main menu appears with four options:
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit

Each option runs a specific function from `contacts.py`.  
The data file `contacts.csv` is automatically created (if it doesn’t exist) and updated every time the user performs an operation.

### File Structure
- `contacts.py`: Main source code of the project (program logic and user interaction).
- `contacts.csv`: The database file storing contact names and phone numbers.
- `README.md`: This file (project documentation and explanation).

### Design Choices
I chose to use a **CSV file** instead of a database like SQLite to keep the project lightweight and easy to understand.  
Each feature is built using functions to make the code modular and maintainable.

### Future Improvements
In future versions, I plan to:
- Add email fields
- Use a graphical interface (Tkinter or Flask)
- Improve search to handle partial matches

This project demonstrates file handling, data persistence, and menu-driven user interaction in Python.

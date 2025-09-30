<<<<<<< HEAD
contacts = {}

# Add Contact
def add_contact(name, number):
    if name in contacts:
        print(f"{name} already exists.")
    else:
        contacts[name] = number
        print(f"Contact {name} added successfully.")

# Delete Contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"{name} not found.")

# Search Contact
def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found.")

# Update Contact
def update_contact(name, number):
    if name in contacts:
        contacts[name] = number
        print(f"{name} updated successfully.")
    else:
        print(f"{name} not found.")

# View All Contacts
def view_contacts():
    if contacts:
        print("All Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# Save Contacts to File
def save_contacts(filename="contacts.txt"):
    with open(filename, "w") as f:
        for name, number in contacts.items():
            f.write(f"{name},{number}\n")  # name and number separated by comma
    print("Contacts saved to file.")

# Load Contacts from File
def load_contacts(filename="contacts.txt"):
    global contacts
    try:
        with open(filename, "r") as f:
            contacts = {}
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    name, number = line.split(",", 1)  # split by first comma
                    contacts[name] = number
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found.")

=======
contacts = {}

# Add Contact
def add_contact(name, number):
    if name in contacts:
        print(f"{name} already exists.")
    else:
        contacts[name] = number
        print(f"Contact {name} added successfully.")

# Delete Contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"{name} not found.")

# Search Contact
def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found.")

# Update Contact
def update_contact(name, number):
    if name in contacts:
        contacts[name] = number
        print(f"{name} updated successfully.")
    else:
        print(f"{name} not found.")

# View All Contacts
def view_contacts():
    if contacts:
        print("All Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# Save Contacts to File
def save_contacts(filename="contacts.txt"):
    with open(filename, "w") as f:
        for name, number in contacts.items():
            f.write(f"{name},{number}\n")  # name and number separated by comma
    print("Contacts saved to file.")

# Load Contacts from File
def load_contacts(filename="contacts.txt"):
    global contacts
    try:
        with open(filename, "r") as f:
            contacts = {}
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    name, number = line.split(",", 1)  # split by first comma
                    contacts[name] = number
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found.")

>>>>>>> 3198bf66210be3919e3762339f090f633b9c33b5

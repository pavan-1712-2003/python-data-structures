<<<<<<< HEAD
from phonebook import add_contact, delete_contact, search_contact, update_contact, view_contacts, save_contacts, load_contacts

def main():
    load_contacts()  # Load saved contacts from text file

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. View All Contacts")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            number = input("Enter new number: ")
            update_contact(name, number)
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            save_contacts()
        elif choice == "7":
            save_contacts()  # Save before exiting
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
=======
from phonebook import add_contact, delete_contact, search_contact, update_contact, view_contacts, save_contacts, load_contacts

def main():
    load_contacts()  # Load saved contacts from text file

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. View All Contacts")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            number = input("Enter new number: ")
            update_contact(name, number)
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            save_contacts()
        elif choice == "7":
            save_contacts()  # Save before exiting
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
>>>>>>> 3198bf66210be3919e3762339f090f633b9c33b5

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    CONTACTS
---------------------------------------------------------------------------------
- File Name: contacts.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn about the procedural programming paradigm
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def display_menu():
    print("Welcome to Contacts Manager")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")        # TODO: Implement the delete contact functionality
    print("5. Update a contact")        # TODO: Implement the update contact functionality
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    contacts[name] = phone
    print("Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts to display.")

def search_contact(contacts):
    search_name = input("Enter the name of the contact to search for: ")
    # TODO: Implement the search functionality
    # Hint: Check if the search_name exists in contacts and display the contact details

def main():
    contacts = {}
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '6':
            print("Thank you for using Contacts Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

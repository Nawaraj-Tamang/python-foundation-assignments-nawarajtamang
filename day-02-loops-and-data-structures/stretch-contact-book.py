"""
Exercise: Contact Book Menu (Stretch)
Student: Nawaraj Tamang
Day: 2
"""

contacts = {}

while True:
    # Display menu
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add contact
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        # Search contact
        name = input("Enter name to search: ")

        if name in contacts:
            details = contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
        else:
            print(f"No contact found with the name '{name}'.")

    elif choice == "3":
        # Delete contact
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"No contact found with the name '{name}'.")

    elif choice == "4":
        # Display all contacts
        if not contacts:
            print("No contacts saved yet.")
        else:
            print("\nAll contacts:")
            for name, details in contacts.items():
                print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")

    elif choice == "5":
        # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
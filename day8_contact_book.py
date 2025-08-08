# Day 8 - Python Dictionaries: Contact Book

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts available.")
    else:
        print("\n📒 Contact List:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def search_contact():
    name = input("Enter name to search: ").strip()
    phone = contacts.get(name)
    if phone:
        print(f"🔍 {name} → {phone}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"🗑 Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
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
        print("👋 Goodbye!")
        break
    else:
        print("⚠ Invalid choice. Try again.")

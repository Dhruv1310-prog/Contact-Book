"""
Command-Line Interface for the Contact Book Application.

This script serves as the main entry point for the user to interact
with the contact book. It provides a menu-driven interface for
adding, viewing, searching, updating, and deleting contacts.
"""
from contact import Contact
from contact_book import ContactBook
from pathlib import Path

def print_menu():
    """
    Displays the main menu of available actions to the user.
    
    This function prints a clear, numbered list of options that the
    user can choose from to interact with the contact book application.
    """

    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    print("-------------------------")

def isValid_phone(phone: str) -> bool:
    """
    Validates a phone number string based on a simple rule.

    Args:
        phone_str (str): The phone number string to validate.

    Returns:
        bool: True if the string contains only digits and allowed characters 
              (+, -, (, ), space), False otherwise.
    """
    
    digits = len(phone)
    if (digits != 10) or (not phone.isnumeric()):
        return False
    return True

        

def main():
    """
    The main function to run the Contact Book application.

    This function initializes the ContactBook, loads existing contacts,
    and enters the main loop to process user commands.
    """
    PROJECT_DIR = Path(__file__).resolve().parent
    JSON_FILE = PROJECT_DIR / "contacts.json"
  
    contact_book = ContactBook()       # Instantiation
    contact_book.load_contacts()

    while True:
        print_menu()
        try:
            user_input = int(input("Enter Your Choice(1-6): "))
            match user_input:
                case 1:
                    print("Enter Contact Details:-")
                    name = input("\tName of Contact: ")
                    while True:
                        phone = input("\tEnter phone number: ")                
                        if isValid_phone(phone):
                            break
                        else:
                            print("Incorrect Phone Number.\nTry Again")
                    phone_to_show = phone[0:5] + " " + phone[5:10]
                    
                    while True:
                        existEmail = input("Does Contact Have a Email ID[y/n]:")
                        if existEmail.lower() == 'n':
                            email = None
                            break
                        elif existEmail.lower() == 'y':
                            while True:
                                email = input("\tEnter Email ID: ")
                                if '@' in email and '.' in email and email.find('@') < email.find('.'):
                                    break
                                else:
                                    print("Incorrect Format of Email.\nTry Again")
                            break
                        else:
                            print("Invalid Input")
                    new_contact = Contact(name,phone_to_show, email)
                    contact_book.add_contact(new_contact)
                case 2:
                    contact_book.view_contact()
                case 3:
                    contact_to_search = input("Enter CONTACT NAME to be searched: ")
                    result = contact_book.search_contact(contact_to_search)
                    if not result:
                        print(f"No contact named {contact_to_search}")
                    else:
                        print(f"Search Result: {len(result)} Found")
                        print("\n*******************************\n")
                        for contact in result:
                            print(contact)                
                    print("\n*******************************\n")
                case 4:
                    print("You wish to update a contact")
                    print("\n*******************************\n")
                                    
                    name_query = input("Name of Contact Or Enter Serial Number:")          
                    new_phone = None
                    new_email = None
                    while True:
                        choice = int(input("\n1. Phone Number\n2. Email\n3. Phone Number And Email\nEnter Update Method: "))
                        match choice:
                            case 1:
                                new_phone = input("\tNew Phone Number:")
                                break
                            case 2:
                                new_email = input("\tNew Email:")
                                break
                            case 3:
                                new_phone = input("\tNew Phone Number:")
                                new_email = input("\tNew Email:")
                                break
                            case _:
                                print("Wrong Input!!!\nTry Again")

                    identifier = None
                    try:
                        identifier = int(name_query)  # For index value
                    except ValueError:
                        identifier = name_query

                    if contact_book.update_contact(identifier, new_phone= new_phone, new_email= new_email):
                        print("Contact Successfully Updated")
                    else:
                        print(f"Error: Contact {name_query} not found")

                case 5:
                    print("You Wish to delete a contact")
                    name_query = input("Name of Contact Or Enter Serial Number:")  
                    identifier = None        
                    try:
                        identifier = int(name_query)  # For index value
                    except ValueError:
                        identifier = name_query

                    if contact_book.delete_contact(identifier):
                        print("Contact Successfully Deleted")
                    else:
                        print(f"Error: Contact {name_query} not found\nNo Contact Deleted")

                case 6:
                    print("Have A Nice Day")
                    break
                case _:
                    print("Invalid Choice.\nEnter Choice between 1 and 6...")
        except ValueError:
            print("\nPlease enter the option number\n")
if __name__ == "__main__":
    main()                
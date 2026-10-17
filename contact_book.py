import json
from contact import Contact
from pathlib import Path



class ContactBook:
    """
    Manages a collection of Contact objects.

    This class is responsible for loading contacts from a JSON file,
    saving contacts to the file, and providing methods to add, view,
    search, update, and delete contacts from the collection.

    """

    def __init__(self):
        self.contacts = list()
        self.filename = Path(__file__).resolve().parent / "contacts.json"

    def load_contacts(self):
        """
        Loads the contact list from the JSON file.

        This method will handle opening the file, parsing the JSON data,
        and creating Contact objects to populate the self.contacts list.
        """

        try:
            # Rehydration using list comprehension

            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.contacts = [Contact(**contact_data) for contact_data in data]

        except FileNotFoundError:
            pass

        except json.JSONDecodeError:
            print(f"Warning: Could not decode '{f}'. File may be corrupted or empty. Starting fresh.")
            self.contacts = [] # Starting Fresh

        except IOError as e:
            print(f"Warning: Could not read from '{self.filename}': {e}. Starting with an empty list.")
            self.contacts = [] # Starting Fresh

    def save_contacts(self):
        """
        Saves the current contact list to the JSON file.

        This method serializes the list of Contact objects into a
        list of dictionaries, which is then written to the file.
        """
        try:
            data_to_save = [contact.to_dict() for contact in self.contacts]
            
            with open(self.filename, 'w') as f:

                # json.dump() writes the Python object to the file as a JSON string.
                # - data_to_save: The object we want to save (our list of dictionaries).
                # - f: The file object to write to.
                # - indent=4: This makes the JSON file human-readable by pretty-printing it.

                json.dump(data_to_save, f, indent= 4)
        except IOError as e:
                    print(f"Warning: Could not read from '{self.filename}': {e}. Starting with an empty list.")
                    
    def add_contact(self, contact: Contact):
            """
        Adds a new contact to the contact book.

        Args:
            contact (Contact): The Contact object to be added.
                               It is expected to be a fully-formed instance
                               of the Contact class.
        """
            self.contacts.append(contact)
            self.save_contacts()
    
    def view_contact(self):
        """
        Displays all contacts in the contact book.

        If the book is empty, it prints a message. Otherwise, it prints
        an indexed list of all contacts.
        """
        if not self.contacts:
        # (len(self.contacts) == 0)
            print("Your Contact Book is EMPTY")
        else:
            for index, contact in enumerate(self.contacts, start = 1):
                print(f"{index}. {contact}")
            print("\n***********************************************\n")

    def search_contact(self, name_query: str) -> list:
        """
        Searches for contacts by name.

        The search is case-insensitive. It will find all contacts where
        the query string is a substring of the contact's name.

        Args:
            name_query (str): The name (or part of the name) to search for.

        Returns:
            list: A list of Contact objects that match the query. 
                  Returns an empty list if no matches are found.
        """
        result = []
        for contact in self.contacts:
            # if(contact.name.lower() == name_query.lower): user must know the full name of contact what if he dont
            if  name_query.lower() in contact.name.lower():
                result.append(contact)
        return result

    def delete_contact(self, identifier: str | int) -> bool:
        """
        Deletes a contact identified by its name or 1-based index.

        Args:
            identifier (str | int): The name (case-insensitive) or the 1-based index 
                                    of the contact to delete.

        Returns:
            bool: True if a contact was deleted, False otherwise.
        """
        contact_to_delete = None

        if isinstance(identifier , int):
            index = identifier-1
            if 0 <= index < len(self.contacts):
                contact_to_delete = self.contacts[index]   
        elif isinstance(identifier, str):
            for contact in self.contacts:
                if identifier.lower() == contact.name.lower():
                    contact_to_delete = contact
                    break

        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            self.save_contacts()
            return True
        
        return False

    def update_contact(self, identifier: str| int, new_phone: str, new_email: str) -> bool:
        """
        Updates the phone number and/or email of an existing contact.

        The contact is identified by its name or 1-based index.
        The update is partial: if new_phone or new_email is an empty string,
        that field will not be updated.

        Args:
            identifier (str | int): The name or index of the contact to update.
            new_phone (str): The new phone number.
            new_email (str): The new email address.

        Returns:
            bool: True if the contact was found and updated, False otherwise.
        """

        contact_to_update = None
        if isinstance(identifier, int):
            index = identifier -1
            if 0 <= index < len(self.contacts):
                contact_to_update = self.contacts[index]
        elif isinstance(identifier, str):
            for contact in self.contacts:
                if(contact.name.lower() == identifier.lower()):
                    contact_to_update = contact
                    break
        if contact_to_update:
            if new_phone:
                contact_to_update.phone = new_phone
            if new_email:
                contact_to_update.email = new_email
            self.save_contacts()
            return True
        return False
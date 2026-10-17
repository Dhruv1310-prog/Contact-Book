class Contact:        # Class follows PascalCase and Functions uses snakecase
    """
    Represents a single contact with a name, email address
    and phone number

    """

    def __init__(self, name, phone, email):
        """
        Initializes a new Contact object.
        The 'self' parameter refers to the instance of the object being created.
        
         'self' is still the first parameter, which Python handles automatically.
         'name', 'phone', and 'email' are the parameters that will accept the data needed to create a new contact.
        """

        self.name = name   # Instance attribute - name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Returns a user-friendly string representation of the Contact object.
        
        This method is called by built-in functions like print() and str().
        It must return a string.
        
        """
        
        return f"Name: {self.name:<15}\tPhone Number: {self.phone}\tEmail: {self.email}"

    def to_dict(self):
    # This method is for serialization. It provides a machine-readable
    # representation of the object, which is ideal for saving to files (like JSON)

        """
        Converts the Contact object to a dictionary.

        This is a common pattern for preparing an object for JSON serialization.
        
        Returns:
            dict: A dictionary containing the contact's data
        """
        return {
                "name": self.name,
                "phone": self.phone,
                "email": self.email
                }
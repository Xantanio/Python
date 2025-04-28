'''
O código está todo escrito e comentado em inglês exceto por essa descrição inicial em específico.
O código implementa todas as funções requisitadas, todavia acrescentei algumas funcionalidades como delete e update.
Decidi por criar duas classes: User e Bank, para facilitar o entedimento e a escalabilidade do código.
A função main() faz a testagem do código
'''

class User:
    """Represents a bank user with personal information"""
    
    def __init__(self, name, email, age):
        """
        Initialize a new User object
        
        Args:
            name (str): User's full name
            email (str): User's email address
            age (int): User's age
        """
        self.name = name    # User's name
        self.email = email  # User's email address
        self.age = age      # User's age

    def getName(self):
        """Get the user's name"""
        return self.name
    
    def getEmail(self):
        """Get the user's email address"""
        return self.email
    
    def getAge(self):
        """Get the user's age"""
        return self.age


class Bank:
    """Represents a banking system that manages User objects"""
    
    def __init__(self):
        """Initialize an empty bank with no users"""
        self.bank = []  # List to store User objects
    
    def printInfo(self):
        """
        Print information for all users in the bank
        
        Returns:
            bool: True if users were printed, False if bank is empty
        """
        if not self.bank:  # Check if bank is empty
            print("Bank is empty.")
            return False
        else:
            # Print each user's information with line breaks
            for user in self.bank:
                print(f"Name: {user.name}\nE-mail: {user.email}\nAge: {user.age}\n")
            return True

    def printUser(self, name):
        """
        Print information for a specific user
        
        Args:
            name (str): Name of user to find
            
        Returns:
            bool: True if user was found and printed, False otherwise
        """
        for user in self.bank:
            if user.name == name:  # Check each user's name
                print(f"Name: {user.name}\nE-mail: {user.email}\nAge: {user.age}\n")
                return True
        print("User not found.")
        return False

    def findUser(self, name):
        """
        Find a user by name
        
        Args:
            name (str): Name of user to find
            
        Returns:
            User: User object if found, None otherwise
        """
        for user in self.bank:
            if user.name == name:
                return user
        print("User not found.")
        return None

    def registerUser(self, user):
        """
        Register a new user in the bank
        
        Args:
            user (User): User object to register
            
        Returns:
            bool: True if registration succeeded, False if user exists
        """
        if not self.bank:  # If bank is empty, add first user
            self.bank.append(user)
            return True
        else:
            if not self.findUser(user.name):  # Check if user exists
                self.bank.append(user)
                print(f"User {user.name} registered.")
                return True
            else:
                print("User already registered.")
                return False

    def deleteUser(self, name):
        """
        Delete a user from the bank
        
        Args:
            name (str): Name of user to delete
            
        Returns:
            bool: True if deletion succeeded, False otherwise
        """
        if not self.bank:  # Check if bank is empty
            print("Cannot delete from empty bank.")
            return False
        else:
            user = self.findUser(name)
            if user:  # If user exists
                self.bank.remove(user)
                print(f"User {name} removed.")
                return True
            else:
                print("User not found.")
                return False
    
    def updateUser(self, name, new_data):
        """
        Update user information
        
        Args:
            name (str): Name of user to update
            new_data (dict): Dictionary of attributes to update (e.g., {'email': 'new@email.com'})
            
        Returns:
            bool: True if update succeeded, False otherwise
        """
        if not self.bank:  # Check if bank is empty
            print("Bank is empty.")
            return False
        
        user = self.findUser(name)
        if user:
            # Update each attribute in new_data if it exists
            for key, value in new_data.items():
                if hasattr(user, key):  # Check if attribute exists
                    setattr(user, key, value)  # Update attribute
            print(f"User {name} updated successfully.")
            return True
        return False



def main():
    # Create a bank instance
    my_bank = Bank()

    # Test 1: Print info of empty bank
    print("\n--- Test 1: Print empty bank ---")
    my_bank.printInfo()

    # Test 2: Register users
    print("\n--- Test 2: Register users ---")
    user1 = User("Alice", "alice@example.com", 25)
    user2 = User("Bob", "bob@example.com", 30)
    user3 = User("Charlie", "charlie@example.com", 35)
    
    my_bank.registerUser(user1)
    my_bank.registerUser(user2)
    my_bank.registerUser(user3)
    
    # Try to register duplicate user
    my_bank.registerUser(User("Alice", "newalice@example.com", 26))

    # Test 3: Print all users
    print("\n--- Test 3: Print all users ---")
    my_bank.printInfo()

    # Test 4: Find and print specific user
    print("\n--- Test 4: Find and print user ---")
    my_bank.printUser("Bob")
    my_bank.printUser("Unknown")  # Non-existent user

    # Test 5: Update user
    print("\n--- Test 5: Update user ---")
    my_bank.updateUser("Alice", {"email": "alice_new@example.com", "age": 26})
    my_bank.printUser("Alice")

    # Test 6: Delete user
    print("\n--- Test 6: Delete user ---")
    my_bank.deleteUser("Bob")
    my_bank.deleteUser("Unknown")  # Non-existent user
    my_bank.printInfo()

    # Test 7: Edge cases
    print("\n--- Test 7: Edge cases ---")
    empty_bank = Bank()
    empty_bank.deleteUser("Nobody")  # Delete from empty bank
    empty_bank.updateUser("Ghost", {"age": 100})  # Update in empty bank

if __name__ == "__main__":
    main()
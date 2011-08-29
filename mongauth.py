"""
User authentication in pymongo.

PyMongo + Authentication  
Super simple.
Super fun.
Uses the bcrypt library to be very, very secure.
Will not store any other user data, by design.
You can keep that stuff elsewhere.
"""

import bcrypt

DEFAULT_SEC = 12

class Mongauth:
    """
    The object you need to instantiate to use Mongauth.
    
    You basically only need one per application.
    Could make another one to have different levels of security.
    """

    def __init__(self, collection, security=DEFAULT_SEC):
        """
        Makes a Mongauth object.
        
        Collection should be a pymongo collection
        Security should be an integer.  
        The default is 12.  
        Raising the number produces a security/speed trade-off.
        """
        self.collection = collection
        self.collection.ensure_index("user",unique=True)
        self.security = security

    def new(self, user, pw):
        """
        Creates a new user.

        Returns True if it generates a new user in the collection.  
        Returns False if not.  
        Will throw an OperationError if it can't insert the new user.
        """
        if self.collection.find_one({"user":user}):
            return False
        else:
            self.collection.insert({"user":user, "pw":self.__transform(pw)}, safe=True)
            return True

    def admin_destroy(self, user):
        """
        Removes a user unconditionally.

        Returns True if it removes the user.
        Returns False otherwise.
        Does not require a password.  
        Should never be accessible to an end-user.  
        Will throw an OperationError if it runs into network issues.
        """
        if self.collection.remove({"user":user}, safe=True)["n"] > 0:
            return True
        else:
            return False

    def destroy(self, user, pw):
        """
        Removes a user.
        
        Returns True if it removes the user. 
        Return False otherwise.
        Requires a password.  
        Should be accessible to an end-user.  
        Will throw an OperationError if it runs into network issues.
        """
        if self.auth(user,pw):
            if self.collection.remove({"user":user}, safe=True)["n"] > 0:
                return True
        return False

    def auth(self, user, pw):
        """
        Authenticates a user/password pair.

        Returns True if it finds that your username and password match up. 
        Returns False otherwise.
        """
        user = self.collection.find_one({"user":user})
        if user:
            if bcrypt.hashpw(pw, user["pw"]) == user["pw"]:
                return True
        return False

    def obliterate(self):
        """
        Forgets all of your user information.  

        Really all of it.  Probably should not be exposed to end-users.  
        Returns True if it removes data.
        Returns False otherwise.
        Mostly used for testing.  
        Will throw an OperationError if it runs into network issues.
        """
        if self.collection.remove(safe=True)["n"] > 0:
            return True
        else:
            return False

    def __transform(self, pw):
        return bcrypt.hashpw(pw, bcrypt.gensalt(self.security))

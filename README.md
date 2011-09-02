#Mongauth

##Premise
PyMongo + Authentication  
Super simple.
Super fun.

##Installation
if you have pip:
   pip install mongauth
else:
   download source from https://github.com/mnn2104/mongauth and run:
`python setup.py install`

##Dependencies
py-bcrypt
pymongo (just need a collection, Mongauth doesn't actually ever import pymongo)

##How to use
```python
from mongauth import Mongauth
from pymongo import Connection
collection = Connection().awesomedb.supercollection
auth = Mongauth(collection) #making the mongauth object

auth.new("username","password") #creating your account
auth.auth("username","passowrd") #oops you made a typo 
auth.auth("username","password") #there you go
auth.destroy("username","penis") #someone is trying to delete your account!
auth.destroy("username","password") #oh, I guess it's you.
auth.new("username","password") #recreating your account
auth.new("username","password") #you can't do that, you're already in the db!
auth.admin_destroy("username") #I guess you were causing trouble.
```

##Test
Assumes you have a non-password protected mongod running locally, and that your mongauth db's test collection is empty.

##BCrypt
Everyone gets to use BCrypt!
NB: BCrypt is slow by design, so that someone who is attacking your password store cannot do it efficiently.  If you find that you can't take how slow it is, change security to something lower when you init your mongauth object.  I found 10 to be pretty fast--the default is 12.  If you are looking for more security than default, be easy on the gas.  Even upping the number by a small amount will make it much slower.

##A note on the backend
I index on user in the collection.  Those users are also unique.

##API

### Mongauth(self, collection, security=DEFAULT_SEC)
Collection should be a pymongo collection, and security should be an integer.  The default is 12.  By making that number higher, you get more secure, but also slower.

### new(self, user, pw)
Returns true if it successfully generates a new user in the collection, false if not.  Will throw an OperationError if it can't insert the new user.

### admin_destroy(self, user)
Returns true if it successfully removes at least one user by that name.  Does not require a password.  Should never be accessible to an end-user.  Will throw an OperationError if it runs into network issues.

### destroy(self, user, pw)
Returns true if it successfully removes at least one user by that name.  Requires a password.  Should be accessible to an end-user.  Will throw an OperationError if it runs into network issues.

### auth(self, user, pw)
Authenticates a user/password pair.  Returns true if it finds that your username and password match up. Returns false otherwise.

### obliterate(self)
Forgets all of your user information.  Really all of it.  Probably should not be exposed to end-users.  Mostly used for testing.  Will throw an OperationError if it runs into network issues.

##FAQ
Q:  
Do you support python3?  
A:  
Not until bcrypt is ported over to python 3.
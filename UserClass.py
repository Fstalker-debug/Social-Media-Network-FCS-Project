# this file contains the class user and all of its methods

class user: 

    def __init__(self, firstName=None, lastName=None, username=None, ID=None, email=None, Bio=None)->None:
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.ID = ID
        self.email = email
        self.Bio = Bio
        self.username_log = []
        pass

    def displayUser(self):

        return "firstname: " + self.firstName + "\n" + "lastName: " + self.lastName + "\n" + "UserName: " + self.username + "\n" + "Bio: " + self.Bio

    def createUsername(self):
        username = input("Please create a new username: ")
        while username  in self.username_log:
            username = input("Username already take, Please provide a new one: ")
        self.username_log.append(username)
        return username
    
    def createUser(self):
        self.firstName = input("Please enter your First Name: ")
        self.lastName = input("Please enter your Last Name: ")
        self.username = self.createUsername()
        self.ID = input("Please enter your ID: ")
        self.email = input("Please enter your email: ")
        self.Bio = input("Please enter your Bio: ")

User1 = user()
User1.createUser()

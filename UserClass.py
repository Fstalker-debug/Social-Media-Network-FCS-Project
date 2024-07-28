# this file contains the class user and all of its methods

class user: 
    
    username_log = []

    def __init__(self, firstName=None, lastName=None, username=None, ID=None, email=None, Bio=None, FriendList=None)->None:
        if FriendList is None:
            FriendList = []
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.ID = ID
        self.email = email
        self.Bio = Bio
        self.FriendList = FriendList

        if username is not None:
            user.username_log.append(username)
        else:
            raise ValueError(f"username: {username} is already taken")
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
        self.username = self.createUsername(user)
        self.ID = input("Please enter your ID: ")
        self.email = input("Please enter your email: ")
        self.Bio = input("Please enter your Bio: ")
        ## later on i need to check i should allow to add the username of Friends from here
    
    @classmethod
    def getListUsers(cls):

        return cls.username_log
    
    def addFriend(self, user_name):
        
        if user_name not in self.FriendList:
            
            self.FriendList.append(user_name)

    def rmvFriend(self, user1, user2):

        if user1 in self.FriendList and user2 in self.FriendList:
            pass

    def printfriends(self):
            
            return self.FriendList ## will it give the list of Friends just for this username
        


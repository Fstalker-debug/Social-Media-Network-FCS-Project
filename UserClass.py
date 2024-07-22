# this file contains the class user and all of its methods

class user: 
    
    username_log = []

    def __init__(self, firstName=None, lastName=None, username=None, ID=None, email=None, Bio=None)->None:
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.ID = ID
        self.email = email
        self.Bio = Bio
        self.FriendList = []

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
        self.username = self.createUsername()
        self.ID = input("Please enter your ID: ")
        self.email = input("Please enter your email: ")
        self.Bio = input("Please enter your Bio: ")
    
    @classmethod
    def getListUsers(cls):

        return cls.username_log
    
    def addFriend(self, user1, user2):
        
        if user1 not in self.FriendList and user2 not in self.FriendList:
            
            self.FriendList.append(user2)

    def rmvFriend(self, user1, user2):

        if user1 in self.FriendList and user2 in self.FriendList:
            pass

    def userFriendList(self, username):

        if username in self.username_log:
            return self.FriendList() ## will it give the list of Friends just for this username
        pass

################################################
## TESTING ###########                          #
################################################

user1 = user("bob","james","bob_james","B283","bob_james@gmail.com","Hello world")
user2 = user("lolipop","lebron","lebron_lolipop","B293","lebron_lolipop@gmail.com","HI lolo world")
user3 = user("Brian","kpop","brian_kpop","B285","brian_kpop@gmail.com","I am sexy")
user4 = user("Smith","kurky","smith_kurky","B383","smith_kurky@gmail.com","Hola world")
user5 = user("Barron","Trump","Barron Tr","B283","Barron_trump@hotmail.com","I am the president of the united states of America")

print(user5.displayUser())

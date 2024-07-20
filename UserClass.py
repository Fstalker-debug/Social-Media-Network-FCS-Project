# this file contains the class user and all of its methods

class user:
    def __init__(self, firstName, lastName,email, Age, location, ID):

        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        self.location = location
        self.ID = ID
        self.email = email
    def revealInfo(self):
        dict = {"K112345": "James"}
        print("first Name is ", end="")
        print(self.firstName)
        print("last Name is ", end="")
        print(self.lastName)


user1 = user("James","Bond","jamesbond007@gmail.com", 27, "Detroit", "K112345")
user1.revealInfo()


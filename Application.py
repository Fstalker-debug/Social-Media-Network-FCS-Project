##### here is the main application ####
from UserClass import user
from GraphClass import graph 

NetworkGraph = graph()

user1 = user("bob","james","bob_james","B283","bob_james@gmail.com","Hello world",["lebron_lolipop","Barron Tr"])
user2 = user("lolipop","lebron","lebron_lolipop","B293","lebron_lolipop@gmail.com","HI lolo world",["smith_kurky"])
user3 = user("Brian","kpop","brian_kpop","B285","brian_kpop@gmail.com","I am sexy",["Barron Tr"])
user4 = user("Smith","kurky","smith_kurky","B383","smith_kurky@gmail.com","Hola world",["bob_james"])
user5 = user("Barron","Trump","Barron Tr","B283","Barron_trump@hotmail.com","I am the president of the united states of America",["brian_kpop"])

## important to note that i should always be passing the username of the user

## 1) add users to the graph (using their username)

NetworkGraph.addUserToGraph(user1.username)
NetworkGraph.addUserToGraph(user2.username)
NetworkGraph.addUserToGraph(user3.username)
NetworkGraph.addUserToGraph(user4.username)
NetworkGraph.addUserToGraph(user5.username)

## 2) create a connection between two users (using also their username)

NetworkGraph.addConnection(user1.username, user2.username)
NetworkGraph.addConnection(user1.username, user3.username)
NetworkGraph.addConnection(user1.username, user4.username)

NetworkGraph.addConnection(user4.username, user5.username)

connections = NetworkGraph.displayConnections()

print(connections)

NetworkGraph.rmvConnection(user1.username,user3.username)

print(NetworkGraph.displayConnections())

## testing 

# user1.addFriend("smith_kurky")
# user1.addFriend("Alexandro007")

# print(connections)
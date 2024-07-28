################################################
## TESTING ###########                          #
################################################

user1 = user("bob","james","bob_james","B283","bob_james@gmail.com","Hello world",["lebron_lolipop"])
user2 = user("lolipop","lebron","lebron_lolipop","B293","lebron_lolipop@gmail.com","HI lolo world",["smith_kurky"])
user3 = user("Brian","kpop","brian_kpop","B285","brian_kpop@gmail.com","I am sexy",["Barron Tr"])
user4 = user("Smith","kurky","smith_kurky","B383","smith_kurky@gmail.com","Hola world",["bob_james"])
user5 = user("Barron","Trump","Barron Tr","B283","Barron_trump@hotmail.com","I am the president of the united states of America",["brian_kpop"])


print(user1.FriendList) ## because i am printing it directly i am not getting the result i want

print(user1.showFriends())
# user1.addFriend(user2.username) => doesn't work
user1.addFriend("brian_kpop")

print(user1.showFriends())


## test the create a user method 

# x = user.createUser(user)

###########
# testing #
###########

# Uncomment to test

# network_graph = Graph()

# ## add users to the graph (adding vertices)
# network_graph.add_user("user1")
# network_graph.add_user("user2")
# network_graph.add_user("user3")
# network_graph.add_user("user4")

# ## add connections/edges between users
# network_graph.add_connection("user1", "user2")
# network_graph.add_connection("user2", "user3")
# network_graph.add_connection("user2", "user4")

# network_graph.display_connections()

# print(network_graph.show_created_users())

# network_graph.remove_user("user3")

# print(network_graph.show_created_users())

# ## implementation for BFS algorithm
# network_graph.bfs("user1")

# network_graph.dfs("user1")



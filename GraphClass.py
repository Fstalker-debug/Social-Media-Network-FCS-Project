# from collections import deque

# class graph:

#     numberofusers = 0

#     def __init__(self):

#         self.vertices = []
#         self.graph = {}

#     def addUserToGraph(self, user):

#         if user not in self.vertices:
#             self.vertices.append(user)
#             self.graph[user] = []
#             self.numberofusers += 1

#     def rmvUserfromGraph(self, user1):

#         self.vertices.remove(user1)

#     def addConnection(self, user1, user2):
        
#         if user1 in self.vertices and user2 in self.vertices:

#             self.graph[user1].append(user2)
        

#     def rmvConnection(self,user1, user2):

#         if user1 in self.vertices and user2 in self.vertices:
#             self.graph[user1].remove(user2)
#         pass

#     def showcreatedUsers(self):

#         return self.vertices
    
#     def BFS(self, start_node):
#         visited = {node: False for node in self.vertices}
#         q = deque()
#         q.append(start_node)
#         visited[start_node] = True

#         while q:
#             current_node = q.popleft()
#             print(current_node, end=" ")

#             for neighbor in self.graph[current_node]:
#                 if not visited[neighbor]:
#                     q.append(neighbor)
#                     visited[neighbor] = True


#     # A helper function for DFS function
#     def DFSUtil(self, user, visited):
 
#         # Mark the current node as visited and it will print it
#         visited.add(user)
#         print(user, end=' ')

#         for neighbour in self.graph[user]:
#             if neighbour not in visited:
#                 self.DFSUtil(neighbour, visited)
 
     
#     # Depth-first search algorithm
#     def DFS(self, user):
 
#         # Create a set to store visited vertices
#         visited = set()
 
#         self.DFSUtil(user, visited)




#     def displayConnections(self):
#         for user, connections in self.graph.items():
#             print(f"{user} is connected to: {', '.join(connections)}")

#         # return self.graph()
    
#     @classmethod
#     def nb_vertices(cls):

#         return cls.numberofusers




# ###########
# # testing #
# ###########

# # network_graph = graph()

# # ## add users to the graph (adding vertices)

# # network_graph.addUserToGraph("user1")
# # network_graph.addUserToGraph("user2")
# # network_graph.addUserToGraph("user3")
# # network_graph.addUserToGraph("user4")

# # ## add connections/edges between users

# # network_graph.addConnection("user1" , "user2")
# # network_graph.addConnection("user2" ,"user3")
# # network_graph.addConnection("user2" ,"user4")

# # print(network_graph.displayConnections())


# # print(network_graph.showcreatedUsers())

# # # network_graph.rmvUserfromGraph("user3")

# # # print(network_graph.showcreatedUsers())

# # ## implementation for my BFS algorithm
# # vertices = network_graph.numberofusers
# # network_graph.BFS("user1")

# # network_graph.DFS("user1")


from collections import deque

class graph:
    def __init__(self):
        self.vertices = []
        self.graph = {}

    def addUserToGraph(self, user):
        if user not in self.vertices:
            self.vertices.append(user)
            self.graph[user] = []

    def remove_user(self, user):
        if user in self.vertices:
            self.vertices.remove(user)
            del self.graph[user]
            for connections in self.graph.values():
                if user in connections:
                    connections.remove(user)

    def addConnection(self, user1, user2):
        if user1 in self.vertices and user2 in self.vertices:
            if user2 not in self.graph[user1]:
                self.graph[user1].append(user2)
            if user1 not in self.graph[user2]:  # Assuming undirected graph
                self.graph[user2].append(user1)

    def remove_connection(self, user1, user2):
        if user1 in self.vertices and user2 in self.vertices:
            if user2 in self.graph[user1]:
                self.graph[user1].remove(user2)
            if user1 in self.graph[user2]:  # Assuming undirected graph
                self.graph[user2].remove(user1)

    def show_created_users(self):
        return self.vertices
    
    def bfs(self, start_node):
        if start_node not in self.vertices:
            print("Start node not in graph")
            return
        visited = {node: False for node in self.vertices}
        q = deque()
        q.append(start_node)
        visited[start_node] = True

        while q:
            current_node = q.popleft()
            print(current_node, end=" ")

            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
        print()

    def DFS_UTIL(self, user, visited):
        visited.add(user)
        print(user, end=' ')

        for neighbour in self.graph[user]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def DFS(self, user):
        if user not in self.vertices:
            print("Start node not in graph")
            return
        visited = set()
        self.dfs_util(user, visited)
        print()

    def displayConnections(self):
        for user, connections in self.graph.items():
            print(f"{user} is connected to: {', '.join(connections)}")

    @property
    def number_of_users(self):
        return len(self.vertices)
    
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



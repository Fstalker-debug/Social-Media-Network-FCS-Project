from collections import deque

class graph:

    numberofusers = 0

    def __init__(self):

        self.vertices = []
        self.graph = {}

    def addUserToGraph(self, user):

        if user not in self.vertices:
            self.vertices.append(user)
            self.graph[user] = []
            self.numberofusers += 1

    def rmvUserfromGraph(self, user1):

        self.vertices.remove(user1)

    def addConnection(self, user1, user2):
        
        if user1 in self.vertices and user2 in self.vertices:

            self.graph[user1].append(user2)
        

    def rmvConnection(self,user1, user2):

        if user1 in self.vertices and user2 in self.vertices:
            self.graph[user1].remove(user2)
        pass

    def showcreatedUsers(self):

        return self.vertices
    
    def BFS(self, start_node, visited):

        q = deque()
        q.append(start_node)
        visited[start_node] = True

        while q:

            current_node = q.popleft()
            print(current_node, end="")

            for neighbor in self.graph:

                if neighbor not in visited.get(neighbor, False):

                    q.append(neighbor)
                    visited[neighbor] = True
    
    def BFS2(self, start_node):
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


    def displayConnections(self):

        return self.graph
    
    @classmethod
    def nb_vertices(cls):

        return cls.numberofusers




###########
# testing #
###########

network_graph = graph()

## add users to the graph (adding vertices)

network_graph.addUserToGraph("user1")
network_graph.addUserToGraph("user2")
network_graph.addUserToGraph("user3")
network_graph.addUserToGraph("user4")

## add connections/edges between users

network_graph.addConnection("user1" , "user2")
network_graph.addConnection("user2" ,"user3")
network_graph.addConnection("user2" ,"user4")

print(network_graph.displayConnections())


print(network_graph.showcreatedUsers())

# network_graph.rmvUserfromGraph("user3")

# print(network_graph.showcreatedUsers())

## implementation for my BFS algorithm
vertices = network_graph.numberofusers
network_graph.BFS2("user1")


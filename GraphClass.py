class graph:
    
    def __init__(self):

        self.vertices = []
        self.graph = {}

    def addUserToGraph(self, user):

        if user not in self.vertices:
            self.vertices.append(user)
            self.graph[user] = []

    def addConnection(self, user1, user2):
        
        if user1 in self.vertices and user2 in self.vertices:

            self.graph[user1].append(user2)
        

    def rmvConnection(self,user1, user2):

        if user1 in self.vertices and user2 in self.vertices:
            self.graph[user1].remove(user2)
        pass

    def displayConnections(self):

        return self.graph




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


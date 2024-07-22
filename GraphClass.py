class graph:
    
    def __init__(self):

        self.connections = []
        self.graph = {}

    def addConnection(self, user, list):

        self.graph[user] = list

    def displayConnections(self):

        return self.graph




#####
# testing
###########

network_graph = graph()

network_graph.addConnection("user1" , ["user2" , "user3"])
network_graph.addConnection("user2" , ["user1" , "user4"])
network_graph.addConnection("user5" , ["user6" , "user13"])

print(network_graph.displayConnections())


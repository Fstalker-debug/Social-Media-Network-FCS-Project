class graph:
    
    def __init__(self):

        self.node = {} # i will store here users
        self.graph = []

    def addUsertoGraph(self, node):

        if node not in self.node:

            self.node[node] = len(self.graph)

            for row in self.graph:
                row.append(0)
            self.graph.append([0]*(len(self.node)+1))

#####################################################################################
# TESTING LAB###
#####################################################################################

graph = graph()
graph.addUsertoGraph("User1")
graph.addUsertoGraph("User2")
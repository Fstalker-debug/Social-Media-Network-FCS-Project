class graph:
    
    def __init__(self):

        self.vertices = {} # i will store here users
        self.graph = []

    def addUsertoGraph(self, vertex):

        if vertex not in self.vertices:

            self.vertices[vertex] = len(self.graph)

            for row in self.graph:
                row.append(0)
            self.graph.append([0]*(len(self.graph)+1))

    def DisplayGraph(self):

        vertices = sorted(self.vertices.keys())
        matrix = [[0]*len(vertices) for _ in range(len(vertices))]

        for i, row in enumerate(self.graph):
            for j, value in enumerate(row):
                matrix[i][j] = value

        print("  " + " ".join(vertices))
        for i, row in enumerate(matrix):
            print(vertices[i] + "|" + " ".join(map(str, row)))
        
            


#####################################################################################
# TESTING LAB###
#####################################################################################

graph = graph()
graph.addUsertoGraph("User1")
graph.addUsertoGraph("User2")
graph.addUsertoGraph("User3")
graph.addUsertoGraph("User4")
graph.addUsertoGraph("User5")

graph.DisplayGraph()

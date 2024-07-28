from collections import deque


class Graph:

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

    def addConnection(self, user1: str, user2: str):
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

    def dfs_util(self, user, visited):
        visited.add(user)
        print(user, end=' ')

        for neighbor in self.graph[user]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, user):
        if user not in self.vertices:
            print("Start node not in graph")
            return
        visited = set()
        self.dfs_util(user, visited)
        print()

    def displayConnections(self):
        connections = {}
        for node, neighbors in self.graph.items():
            connections[node] = list(neighbors)
        return connections

    @property
    def number_of_users(self):
        return len(self.vertices)
    
    def dijkstra(self, start_user):
        if start_user not in self.vertices:
            print("Start node not in graph")
            return

        # Initialize distances with infinity and set the distance to the start_user to zero
        distances = {user: float('inf') for user in self.vertices}
        distances[start_user] = 0

        # Use a priority queue to store (distance, vertex) tuples
        priority_queue = [(0, start_user)]

        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)

            # If a shorter path to current_user is already known, skip it
            if current_distance > distances[current_user]:
                continue

            for neighbor, weight in self.graph[current_user]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
   
# g = Graph()
# g.addUserToGraph("joujou")
# g.addUserToGraph("loulou")
# g.addUserToGraph("coco")
# g.addConnection("coco", "joujou")
# g.addConnection("coco", "loulou")
# g.addConnection("loulou", "joujou")

# print(g.show_created_users())
# print(g.displayConnections())
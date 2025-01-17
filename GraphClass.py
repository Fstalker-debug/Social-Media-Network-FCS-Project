# from collections import deque
# import heapq


# class Graph:

#     def __init__(self):
#         self.vertices = []
#         self.graph = {}

#     def addUserToGraph(self, user):
#         if user not in self.vertices:
#             self.vertices.append(user)
#             self.graph[user] = []

#     def remove_user(self, user):
#         if user in self.vertices:
#             self.vertices.remove(user)
#             del self.graph[user]
#             for connections in self.graph.values():
#                 if user in connections:
#                     connections.remove(user)

#     def addConnection(self, user1: str, user2: str):
#         if user1 in self.vertices and user2 in self.vertices:
#             if user2 not in self.graph[user1]:
#                 self.graph[user1].append(user2)
#             if user1 not in self.graph[user2]:  # Assuming undirected graph
#                 self.graph[user2].append(user1)

#     def remove_connection(self, user1, user2):
#         if user1 in self.vertices and user2 in self.vertices:
#             if user2 in self.graph[user1]:
#                 self.graph[user1].remove(user2)
#             if user1 in self.graph[user2]:  # Assuming undirected graph
#                 self.graph[user2].remove(user1)

#     def show_created_users(self):
#         return self.vertices

#     def bfs(self, start_node):
#         if start_node not in self.vertices:
#             print("Start node not in graph")
#             return
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
#         print()

#     def dfs_util(self, user, visited):
#         visited.add(user)
#         print(user, end=' ')

#         for neighbor in self.graph[user]:
#             if neighbor not in visited:
#                 self.dfs_util(neighbor, visited)

#     def dfs(self, user):
#         if user not in self.vertices:
#             print("Start node not in graph")
#             return
#         visited = set()
#         self.dfs_util(user, visited)
#         print()

#     def displayConnections(self):
#         connections = {}
#         for node, neighbors in self.graph.items():
#             connections[node] = list(neighbors)
#         return connections

#     @property
#     def number_of_users(self):
#         return len(self.vertices)

#     def dijkstra(self, start_user):
#         if start_user not in self.vertices:
#             print("Start node not in graph")
#             return

#         # Initialize distances with infinity and set the distance to the start_user to zero
#         distances = {user: float('inf') for user in self.vertices}
#         distances[start_user] = 0

#         # List to act as the priority queue
#         priority_queue = [(0, start_user)]

#         while priority_queue:
#             # Extract the user with the smallest distance
#             priority_queue.sort(key=lambda x: x[0])  # Sort by distance
#             current_distance, current_user = priority_queue.pop(0)

#             # Debug print to check the current user and its connections
#             print(f"Processing user: {current_user}, Current distance: {current_distance}")
#             print(f"Connections: {self.graph[current_user]}")

#             # Update distances for neighbors
#             # for neighbor, weight in self.graph[current_user]:
#             #     distance = current_distance + weight
#             #     if distance < distances[neighbor]:
#             #         distances[neighbor] = distance
#             #         priority_queue.append((distance, neighbor))

#         return distances
   
# g = Graph()
# g.addUserToGraph("joujou")
# g.addUserToGraph("loulou")
# g.addUserToGraph("coco")
# g.addConnection("coco", "joujou")
# g.addConnection("coco", "loulou")
# g.addConnection("loulou", "joujou")

# print(g.show_created_users())
# print(g.displayConnections())

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
                connections[:] = [(u, w) for u, w in connections if u != user]

    def addConnection(self, user1: str, user2: str, weight: int):
        if user1 in self.vertices and user2 in self.vertices:
            if not any(u == user2 for u, _ in self.graph[user1]):
                self.graph[user1].append((user2, weight))
            if not any(u == user1 for u, _ in self.graph[user2]):  # Assuming undirected graph
                self.graph[user2].append((user1, weight))

    def remove_connection(self, user1, user2):
        if user1 in self.vertices and user2 in self.vertices:
            self.graph[user1] = [(u, w) for u, w in self.graph[user1] if u != user2]
            self.graph[user2] = [(u, w) for u, w in self.graph[user2] if u != user1]

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

            for neighbor, _ in self.graph[current_node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, user, visited):
        visited.add(user)
        print(user, end=' ')

        for neighbor, _ in self.graph[user]:
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
            connections[node] = [(neighbor, weight) for neighbor, weight in neighbors]
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

        # List to act as the priority queue
        priority_queue = [(0, start_user)]

        while priority_queue:
            # Extract the user with the smallest distance
            priority_queue.sort(key=lambda x: x[0])  # Sort by distance
            current_distance, current_user = priority_queue.pop(0)

            # Debug print to check the current user and its connections
            print(f"Processing user: {current_user}, Current distance: {current_distance}")
            print(f"Connections: {self.graph[current_user]}")

            # Update distances for neighbors
            for neighbor, weight in self.graph[current_user]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    priority_queue.append((distance, neighbor))

        return distances

    def fix_connections(self):
        for user in self.graph:
            self.graph[user] = [(neighbor, 1) if isinstance(neighbor, str) else neighbor for neighbor in self.graph[user]]

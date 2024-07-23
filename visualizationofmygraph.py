import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("A","B")
G.add_edge("A","C")
G.add_edge("A","D")
G.add_edge("D","T")
G.add_edge("B","K")

nx.draw_spring(G, with_labels = True)

plt.show()

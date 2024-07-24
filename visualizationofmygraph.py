from TestCase1 import SocialNetworkWeb
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
users = [
    "user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10",
    "user11", "user12", "user13", "user14", "user15", "user16", "user17", "user18", "user19", "user20",
    "user21", "user22", "user23", "user24", "user25", "user26", "user27", "user28", "user29", "user30",
    "user31", "user32", "user33", "user34", "user35", "user36", "user37", "user38", "user39", "user40",
    "user41", "user42", "user43", "user44", "user45", "user46", "user47", "user48", "user49", "user50",
    "user51", "user52", "user53", "user54", "user55", "user56", "user57", "user58", "user59", "user60",
    "user61", "user62", "user63", "user64", "user65", "user66", "user67", "user68", "user69", "user70",
    "user71", "user72", "user73", "user74", "user75", "user76", "user77", "user78", "user79", "user80",
    "user81", "user82", "user83", "user84", "user85", "user86", "user87", "user88", "user89", "user90",
    "user91", "user92", "user93", "user94", "user95", "user96", "user97", "user98", "user99", "user100"
]

G.add_nodes_from(users)

# Add edges (connections)
connections = [
    ("user1", "user2"), ("user1", "user3"), ("user1", "user47"), ("user1", "user52"), ("user1", "user23"), ("user1", "user35"),
    ("user2", "user39"), ("user2", "user9"), ("user2", "user17"), ("user2", "user7"),
    ("user3", "user96"), ("user3", "user10"), ("user3", "user60"), ("user3", "user86"),
    ("user4", "user5"), ("user4", "user90"), ("user4", "user25"),
    ("user5", "user56"), ("user5", "user83"),
    ("user6", "user33"), ("user6", "user15"), ("user6", "user44"),
    ("user7", "user21"), ("user7", "user92"), ("user7", "user46"),
    ("user8", "user41"), ("user8", "user27"),
    ("user9", "user53"), ("user9", "user11"),
    ("user10", "user84"), ("user10", "user91"),
    ("user11", "user43"), ("user11", "user28"),
    ("user12", "user37"), ("user12", "user95"),
    ("user13", "user65"), ("user13", "user14"),
    ("user14", "user75"), ("user14", "user71"),
    ("user15", "user26"), ("user15", "user57"),
    ("user16", "user58"), ("user16", "user20"),
    ("user17", "user63"), ("user17", "user42"),
    ("user18", "user54"), ("user18", "user87"),
    ("user19", "user73"), ("user19", "user80"),
    ("user20", "user85"), ("user20", "user36"),
    ("user21", "user66"), ("user21", "user55"),
    ("user22", "user81"), ("user22", "user79"),
    ("user23", "user50"), ("user23", "user76"),
    ("user24", "user88"), ("user24", "user62"),
    ("user25", "user72"), ("user25", "user74"),
    ("user26", "user94"), ("user26", "user29"),
    ("user27", "user64"), ("user27", "user32"),
    ("user28", "user70"), ("user28", "user40"),
    ("user29", "user77"), ("user29", "user45"),
    ("user30", "user61"), ("user30", "user18"),
    ("user31", "user49"), ("user31", "user69"),
    ("user32", "user68"), ("user32", "user12"),
    ("user33", "user78"), ("user33", "user24"),
    ("user34", "user48"), ("user34", "user98"),
    ("user35", "user22"), ("user35", "user19"),
    ("user36", "user38"), ("user36", "user67"),
    ("user37", "user31"), ("user37", "user59"),
    ("user38", "user30"), ("user38", "user16"),
    ("user39", "user82"), ("user39", "user34"),
    ("user40", "user51"), ("user40", "user93"),
    ("user41", "user99"), ("user41", "user89"),
    ("user42", "user13"), ("user42", "user1"),
    ("user43", "user60"), ("user43", "user3"),
    ("user44", "user6"), ("user44", "user5"),
    ("user45", "user17"), ("user45", "user68"),
    ("user46", "user8"), ("user46", "user47"),
    ("user47", "user15"), ("user47", "user4"),
    ("user48", "user63"), ("user48", "user21"),
    ("user49", "user72"), ("user49", "user90"),
    ("user50", "user98"), ("user50", "user37")
]

G.add_edges_from(connections)

# Draw the graph
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=50, node_color="blue")
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

plt.title("Social Network Graph")
plt.show()

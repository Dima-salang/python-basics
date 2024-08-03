import networkx as nx
import matplotlib.pyplot as plt


"""
A graph is a non-linear data structure that consists of a collection of nodes (also known as vertices) connected
by edges. It is a fundamental data structure used in various applications, such as computer networks,
social networks, maps, and routing algorithms.

Properties of graphs:

Nodes: Graphs have nodes or vertices, which represent entities or elements. Each node can store data or be associated
with additional attributes.
Edges: Graphs have edges, which represent relationships or connections between nodes. An
edge connects two nodes and can be directed or undirected. Directed edges have a specific direction, while undirected
edges do not.
Connectivity: Graphs can have different levels of connectivity. Some graphs allow any node to be
connected to any other node (complete graph), while others have specific restrictions on connections (sparse graph).
Types of graphs:

Directed Graph (Digraph): In a directed graph, edges have a specific direction. The edges indicate a one-way
relationship, meaning they represent a directed connection from one node to another.

Undirected Graph: In an
undirected graph, edges have no specific direction. The edges represent a bidirectional or symmetric relationship
between nodes.

Weighted Graph: In a weighted graph, each edge has an associated weight or cost. These weights can
represent various properties such as distances, capacities, or costs associated with traversing the edge.

Bipartite
Graph: A bipartite graph consists of two sets of nodes, where nodes in one set are only connected to nodes in the
other set and not within the same set.

Cyclic Graph: A cyclic graph contains at least one cycle, which is a path that
starts and ends at the same node.

Acyclic Graph: An acyclic graph does not contain any cycles. It can be further
classified as a directed acyclic graph (DAG) if it is a directed graph with no cycles.

Connected Graph: A connected
graph is one in which there is a path between any pair of nodes. In other words, there are no isolated nodes or
disconnected components.

Disconnected Graph: A disconnected graph consists of two or more connected components,
where each component is a separate subgraph.

"""

class Node:
    def __init__(self, data):
        self.data = data


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

node1 = Node(15)
node2 = Node(14)
node3 = Node(13)



graph = Graph()

graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)

graph.add_edge(node1, node2)
graph.add_edge(node2, node3)



# NetworkX implementation

netx_graph = nx.Graph()

netx_graph.add_node(node1)
netx_graph.add_node(node2)
netx_graph.add_node(node3)

netx_graph.add_edge(node1, node2)
netx_graph.add_edge(node2, node1)
netx_graph.add_edge(node3, node1)

node_names = {node1: "Node A", node2: "Node B", node3: "Node C"}

pos = nx.spring_layout(netx_graph)
nx.draw(netx_graph, pos, with_labels=True, labels=node_names, node_color='lightblue', node_size=500)
plt.show()



"""
Adding a Node: O(1)

Adding a node to the graph by creating a new entry in the adjacency list dictionary has a constant time complexity.
Removing a Node: O(V + E)

Removing a node involves removing it from the adjacency list and updating the adjacency lists of its neighboring nodes. To remove a node, you need to iterate over its adjacency list and remove references to the node from other nodes' adjacency lists. This operation has a time complexity of O(V + E), where V is the number of nodes and E is the number of edges.
Adding an Edge: O(1)

Adding an edge between two nodes in the adjacency list involves appending the neighboring nodes to each other's adjacency lists. This operation has a constant time complexity.
Removing an Edge: O(V)

Removing an edge involves removing the references to the neighboring nodes from each other's adjacency lists. To do this, you need to iterate over the adjacency list of one node to find the reference to the other node and remove it. The time complexity is O(V) since the worst case is iterating over all the nodes.
Finding Neighbors of a Node: O(1) on average

Accessing the neighbors of a node in an adjacency list representation has a constant time complexity on average. Given a node, you can directly access its adjacent nodes by indexing the adjacency list.
Iterating over Nodes: O(V)

Iterating over all the nodes in the graph by traversing the keys in the adjacency list dictionary takes O(V) time, where V is the number of nodes.
Iterating over Edges: O(E)

Iterating over all the edges in the graph involves traversing the adjacency lists of each node. Since each edge is represented twice (once for each adjacent node), the time complexity is O(E), where E is the number of edges.
"""


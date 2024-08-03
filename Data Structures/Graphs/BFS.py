from queue import Queue
import networkx as nx
from matplotlib import pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, data):
        self.adjacency_list[data] = []

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def bfs_traversal(self, source_node, target_node):
        visited = set()
        bfs_queue = Queue()
        predecessors = {}

        bfs_queue.put(source_node)
        visited.add(source_node)
        predecessors[source_node] = None

        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            print(f"Current Node: {current_node}")

            if current_node == target_node:
                break

            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in visited:
                    bfs_queue.put(neighbor)
                    visited.add(neighbor)
                    predecessors[neighbor] = current_node

        if target_node in visited:
            path = []
            node = target_node
            while node is not None:
                path.append(node)
                node = predecessors[node]
            path.reverse()
            return path

        return None


# Create a graph
netx = nx.Graph()
graph = Graph()

# Add nodes to the graph
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("F")
graph.add_node("G")
graph.add_node("E")

# Add edges to the graph
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "F")
graph.add_edge("F", "A")
graph.add_edge("F", "E")
graph.add_edge("C", "G")
graph.add_edge("C", "E")
graph.add_edge("G", "E")

netx.add_node("A")
netx.add_node("B")
netx.add_node("C")
netx.add_node("D")
netx.add_node("F")
netx.add_node("G")
netx.add_node("E")

netx.add_edge("A", "B")
netx.add_edge("A", "C")
netx.add_edge("C", "F")
netx.add_edge("A", "F")
netx.add_edge("F", "E")
netx.add_edge("B", "D")
netx.add_edge("C", "G")
netx.add_edge("G", "E")
netx.add_edge("C", "E")



# Find the shortest path from "A" to "E"
shortest_path = graph.bfs_traversal("A", "E")

if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print("No path found")


node_names = {"A": "Node A", "B": "Node B", "C": "Node C", "D": "Node D", "E": "Node E", "F":"Node F", "G": "Node G"}

pos = nx.spring_layout(netx)
nx.draw(netx, pos, with_labels=True, labels=node_names, node_color='lightblue', node_size=500)
plt.show()
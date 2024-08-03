"""
Depth-First Search (DFS):

DFS explores the graph in a depth-first manner, visiting as far as possible along each branch before backtracking.
It uses a stack (or the call stack in the recursive version) to keep track of the nodes to be visited.
DFS does not guarantee that it visits all nodes at a particular level before moving to the next level.
It may not find the shortest path between two nodes, as it explores each branch completely before backtracking.
DFS is often used to check for the existence of a path, explore all connected components, or traverse a tree-like structure.
It generally requires less memory compared to BFS because it only needs to store the nodes along the current path.
In summary, BFS explores the graph level by level, while DFS explores it branch by branch. BFS guarantees finding the
shortest path in an unweighted graph, while DFS does not. The choice between BFS and DFS depends on the specific problem
 and the properties of the graph you are working with.


"""


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

    def dfs_traversal(self, source_node):
        visited = set()
        self.dfs_recursive(source_node, visited)

    def dfs_recursive(self, current_node, visited):
        visited.add(current_node)
        print(f"Current Node: {current_node}")

        for neighbor in self.adjacency_list[current_node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)



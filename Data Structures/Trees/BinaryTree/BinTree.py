from collections import deque

# Binary Tree
# Search complexity = O(log n)
# Insert Complexity = O(log n)
# Every iteration we reduce search space by 1/2


# BST Traversal Schemes
# Breadth-first search and Depth-first search


class BSTnode:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

    def insert_node(self, value):
        # if root is null, make new node as root
        if self.value is None:
            self.value = value

        elif self.value == value:
            return
        elif value < self.value:
            if self.leftNode:
                self.leftNode.insert_node(value)
                return
            else:
                self.leftNode = BSTnode(value)
                return
        elif value > self.value:
            if self.rightNode:
                self.rightNode.insert_node(value)
                return
            else:
                self.rightNode = BSTnode(value)
                return

    def get_min(self):
        current = self
        while current.leftNode is not None:
            current = current.leftNode
        return current.value

    def get_max(self):
        current = self
        while current.rightNode is not None:
            current = current.rightNode
        return current.value

    def search(self, target):
        if self is None:
            return None
        elif self.value == target:
            return True
        elif target < self.value:
            return self.leftNode.search(target)
        else:
            return self.rightNode.search(target)

    def delete(self, target):

        # if the tree is empty
        if self is None:
            return None

        # if the value to be deleted is in the left subtree
        elif target < self.value:
            self.leftNode = self.leftNode.delete(target)

        # if the value to be deleted is in the right subtree
        elif target > self.value:
            self.rightNode = self.rightNode.delete(target)
        else:
            # if the node has only one child, simply remove the node
            if self.leftNode is None:
                return self.rightNode
            elif self.rightNode is None:
                return self.leftNode

            # If the node has two children, find the in-order successor
            # (the minimum value in the right subtree) and replace the node
            # with the in-order successor

            min_node = self.get_min()
            self.value = min_node.value
            self.rightNode = self.delete(min_node.value)
        return target

    def in_order_traversal(self):
        # Time Complexity: O(n). Space Complexity: O(n).
        elements = []
        # visit left nodes and get to the smallest value
        if self.leftNode:
            elements += self.leftNode.in_order_traversal()

        # visit current node
        elements.append(self.value)

        # visit right tree
        if self.rightNode:
            elements += self.rightNode.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # O(n) Time complexity
        # O(n) Space complexity

        elements = []
        elements.append(self.value)

        if self.leftNode:
            elements += self.leftNode.pre_order_traversal()

        if self.rightNode:
            elements += self.rightNode.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        # O(n) Time complexity
        # O(n) Space complexity

        elements = []

        if self.leftNode:
            elements += self.leftNode.pre_order_traversal()

        if self.rightNode:
            elements += self.rightNode.pre_order_traversal()

        elements.append(self.value)

        return elements

    def level_order_traversal(self):
        if self is None:
            return None
        results = []
        tree_queue = deque([self])
        while tree_queue:
            popped_node = tree_queue.popleft()
            results.append(popped_node.value)
            if popped_node.leftNode:
                tree_queue.append(popped_node.leftNode)
            if popped_node.rightNode:
                tree_queue.append(popped_node.rightNode)
        return results



node1 = BSTnode(12)
node1.insert_node(13)
node1.insert_node(11)
node1.insert_node(8)
node1.insert_node(9)
print(node1.get_max())
print(node1.in_order_traversal())
print(node1.search(13))
node1.delete(11)
print(node1.in_order_traversal())
print(node1.pre_order_traversal())
print(node1.post_order_traversal())
print(node1.level_order_traversal())





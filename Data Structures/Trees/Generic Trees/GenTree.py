# 	A generic tree is a type of tree data structure where each node can have an arbitrary number of children, unlike a
# 	binary tree where each node can have at most two children. A generic tree can be used to represent a
# 	hierarchical structure, where each node represents an item, and its children represent sub-items.
#
# 	In a generic tree, the root node is the top-level item, and its children represent the sub-items.
# 	Each child node can have its own children, forming a tree-like structure. For example, consider a family tree:
# 	each person is represented by a node, and their children are represented by child nodes.

#     Memory efficient – No extra links are required, hence a lot of memory is saved.
#     Treated as binary trees – Since we are able to convert any generic tree to binary representation,
#     we can treat all generic trees with a first child/next sibling representation as binary trees. Instead of left
#     and right pointers, we just use firstChild and nextSibling.
#     Many algorithms can be expressed more easily because it is just a binary tree.
#     Each node is of fixed size no auxiliary array or vector is required.

# In a generic tree, the position of a new node depends on the application's requirements and the data being stored in
# the tree. If there are no pre-defined rules for determining the position, the developer must implement their own logic
# for determining the position.


# we can use the first child / next sibling representation for an efficient approach to store data since we don't
# have to maintain references to every other child.
# The first child/next sibling representation works by using a linked list structure to represent each node in the tree.
# Each node has two pieces of information:
#
#     A value or data that the node holds.
#
#     A link to the first child of the node, if the node has any children.
#
# If the node has more than one child, the next sibling is represented as another node in the linked list.
# This node has a link to the next sibling and its own value.
#
# This representation makes it possible to traverse the tree and access its nodes efficiently.
# When you want to access a node's children, you simply follow the link to the first child. From there, you can use the
# next sibling links to access all the node's other children.


class GenNode:
    def __init__(self, value):
        self.value = value
        self.first_child = None
        self.next_sibling = None

    def insert_node(self, value):
        if self.value is None:
            self.value = value
        elif

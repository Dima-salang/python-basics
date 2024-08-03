import heapq

"""
Binary trees can be implemented using arrays.
Assuming that a node can be found at index i
then the left child of that node is at 2*i
the right child of that node is at 2*i+1
and the parent node of that node is at i-1//2

a full binary tree is a binary tree in which it is full; no nodes can be inserted at h. Automatically,
all full binary trees are complete binary trees.

a complete binary tree is a binary tree in which there are no gaps in between. meaning that all of the nodes
are continuous up to its height. Even if the binary tree is missing some nodes at the end, it is still complete
if there are no missing nodes in middle. A common definition is that a complete binary tree is a full binary tree
up to 2^h-1 with the last level being filled from left to right. The number of comparisons or swaps in a complete
binary tree is always maximum logn since it depends on its height.
[1, 2, 3, 4, 5, -, -, 6] is a not a complete binary tree because there are missing nodes in the middle.
[1, 2, 3, 4, 5, 6, -, - ] is a binary tree since we are counting from left to right and it doesn't matter if there are
missing nodes at the end.


A heap is a tree-based data structure which is a complete binary tree.
    There are two types of heaps:
    max-heap and min-heap

    In max-heap, the value of the root node must be the greatest among all its child nodes,
    and the same thing must be done for its left and right sub-tree also.

    In min-heap, the value of the root node must be the smallest among all its child nodes,
    and the same thing must be done for its left and right sub-tree also.

    
fast: all operations work in time O(log n) (max_node even works in O(1))
space-efficient: we store an array of priorities; parent-child connections are not stored, but are computed on the fly
easy to implement: all operations are implemented in just a few lines of code
"""


class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def heapify(self, index, size):
        maxIndex = index
        parent = (index - 1) // 2
        left_child = 2*index
        right_child = 2*index + 1

        if index == 0:
            left_child = 2*index+1
            right_child = 2*index+2
        # For Max-Heap
        # If current node is greater than its parent
        # Swap both of them and call heapify again
        # for the parent
        
        # Equivalent for SiftUp function
        if parent >= 0 and self.max_heap[parent] < self.max_heap[index]:
            self.max_heap[index], self.max_heap[parent] = self.max_heap[parent], self.max_heap[index]
            # Recursively heapify the parent node
            self.heapify(parent, size)
        
        # Equivalent for SiftDown functions
        if left_child <= size-1 and self.max_heap[left_child] > self.max_heap[maxIndex]:
            maxIndex = left_child
        if right_child <= size-1 and self.max_heap[right_child] > self.max_heap[maxIndex]:
            maxIndex = right_child
        
        if maxIndex != index:
            self.max_heap[index], self.max_heap[maxIndex] = self.max_heap[maxIndex], self.max_heap[index]
            self.heapify(maxIndex, size)
            


    def insert(self, new_node):
        # insert the new node at the end
        self.max_heap.append(new_node)

        # call heapify on the new node
        if (len(self.max_heap)>1):
            self.heapify(len(self.max_heap)-1, len(self.max_heap))

    def delete(self, index):
        last_element = len(self.max_heap)-1
        self.max_heap[index] = self.max_heap[last_element]
        self.max_heap.pop()

        self.heapify(index, len(self.max_heap))
    
    def change_priority(self, index, new_priority):
        self.max_heap[index] = new_priority
        self.heapify(index, len(self.max_heap))

    def show_heap(self):
        return self.max_heap

    def max_node(self):
        return self.max_heap[0]
    
    def buildMaxHeap(self, arr):
        for node in arr:
            self.insert(node)

class MinHeap:
    def __init__(self):
        self.min_heap = []
        self.size = len(self.min_heap)

    def heapify(self, index):
        parent = (index-1) // 2

        if parent >= 0 and self.min_heap[index] < self.min_heap[parent]:
            self.min_heap[index], self.min_heap[parent] = self.min_heap[parent], self.min_heap[index]
            self.heapify(parent)

    def insert(self, new_node):
        self.min_heap.append(new_node)

        self.heapify(len(self.min_heap) - 1)

    def print_min_heap(self):
        for node in self.min_heap:
            print(node, end=" ")

    def delete(self, index):
        last_element = self.size-1
        self.min_heap[index] = self.min_heap[last_element]
        self.min_heap.pop()

        self.heapify(index)

    def min_node(self):
        return self.min_heap[0]



# one call also use the heapq module in Python.
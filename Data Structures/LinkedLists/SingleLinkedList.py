class Node:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_beginning(self, value):
        # create new node with value
        new_node = Node(value)

        # point new node's next to the current head
        if self.head is not None:
            new_node.next_pointer = self.head

        # appoint head to be the new_node
        self.head = new_node

        self.size += 1

    def insert_end(self, value):

        # create new node with value
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next_pointer:
            last_node = last_node.next_pointer
        last_node.next_pointer = new_node

        self.size += 1

    def insert_middle(self, value, prev_node):

        if prev_node is None:
            return

        new_node = Node(value)

        new_node.next_pointer = prev_node.next_pointer

        prev_node.next_pointer = new_node

        self.size += 1

    def pop_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next_pointer

    def pop(self):
        if self.head is None:
            return
        last_node = self.head
        prev_node = None
        while last_node.next_pointer:
            prev_node = last_node
            last_node = last_node.next_pointer
        prev_node.next_pointer = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.value, end="-->")
            temp = temp.next_pointer

    def count(self):
        return self.size


linked_list = LinkedList()
linked_list.insert_beginning(12)
linked_list.insert_beginning(13)
linked_list.insert_end(15)
linked_list.insert_end(16)
linked_list.insert_end(17)
linked_list.pop_beginning()
linked_list.pop()
linked_list.printlist()

#Singly-linked list

# Main Operations: Insert, Delete
# Auxiliary Operations: Delete List, Count, Find nth node

#Advantages: Simple and easy to use, faster access to elems (constant access)

# Indexing: O(1)
# Insertion at beginning: O(1)
# Insertion at end: O(n)
# Deletion at end: O(n)
# Insertion at middle: O(n)
# Deletion at middle: O(n)
# Wasted Space: O(n) for pointers



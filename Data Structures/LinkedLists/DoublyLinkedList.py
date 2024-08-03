# Doubly-linked lists or DLLs require extra more space with prev pointers.

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_beginning(self, value):

        # create new node
        new_node = Node(value)

        # point the new node's next to the current head
        new_node.next = self.head

        # point the new node's prev to NULL
        new_node.prev = None

        # point the head's prev to the new node
        if self.head is not None:
            self.head.prev = new_node

        # make the new node as head
        self.head = new_node

        self.size += 1

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        last_node = self.head
        # traverse ddl until last pointer
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = None

        self.size += 1

    def pop_beginning(self):
        self.head = self.head.next
        self.head.prev = None

        self.size -= 1

    def pop(self):
        last_node = self.head
        prev_node = None
        while last_node.next:
            prev_node = last_node
            last_node = last_node.next
        prev_node.next = None
        last_node.prev = None

        self.size -= 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end="-->")
            temp = temp.next

    def len(self):
        return self.size


double_linked_list = DoublyLinkedList()
double_linked_list.insert_beginning(12)
double_linked_list.insert_beginning(13)
double_linked_list.insert_beginning(14)
double_linked_list.insert_end(15)
double_linked_list.pop_beginning()
double_linked_list.pop()
double_linked_list.print_list()
print("\n", double_linked_list.len())



# CLLs do not have ends

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CLL:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node is not self.head:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = self.head

    def print_list(self):

        if self.head is None:
            print(self.head)

        temp = self.head
        while temp is not self.head:
            print(temp.value, end="-->")
            temp = temp.next


cll1 = CLL()
cll1.insert_end(1)
cll1.print_list()

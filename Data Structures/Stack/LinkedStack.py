# worst-case scenario, every operation takes constant time
# array implementation is faster

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:  # singly-linked list implementation

    def __init__(self):
        self.head = Node(None)  # dummy head
        self.size = 0

    def is_empty(self):
        return self.head.value is None

    def get_size(self):
        return self.size

    def peek(self):
        print(self.head.value)

    def push(self, item):
        oldHead = self.head
        self.head = Node(item)
        if self.is_empty():
            self.head.next = None
        else:
            self.head.next = oldHead
            self.size += 1

    def pop(self):
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.value


newStack = Stack()
newStack.push(0)
newStack.push(1)
newStack.push(2)
newStack.peek()
print(newStack.size)
newStack.pop()
newStack.peek()
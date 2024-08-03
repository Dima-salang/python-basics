# Enqueue - O(1)
# Dequeue - O(1)
# Front - O(1)
# Rear - O(1)

# using list as a queue implementation is not recommended as inserting or deleting an elem
# at the beginning requires shifting every elem by one which requires O(n).
# we can implement a queue using collection.dequeue which offers O(1) operations


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0

    def is_empty(self):
        return self.head.value is None

    def enqueue(self, item):
        old_tail = self.tail
        self.tail = Node(item)
        self.tail.next = None
        if self.is_empty():
            self.head = self.tail
            self.size += 1
        else:
            old_tail.next = self.tail
            self.size += 1

    def dequeue(self):
        remove = self.head.value
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        self.size -= 1
        return remove

    def front(self):
        print(self.head.value)
        return self.head

    def rear(self):
        print(self.tail.value)
        return self.tail

    def get_size(self):
        return self.size


newQueue = Queue()
newQueue.enqueue("Hello")
newQueue.enqueue("HI there...")
newQueue.enqueue("HIiii")
newQueue.rear()
newQueue.front()
print(newQueue.get_size())

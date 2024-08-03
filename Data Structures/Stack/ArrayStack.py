class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("The stack has no items...")
        else:
            self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("The stack has no items...")
        return self.items[len(self.items) - 1]

    def print_stack(self):
        for item in self.items:
            print(item)


class BinTreeArray:
    def __init__(self):
        self.binary_tree = []

    def insert(self, value):
        self.binary_tree.append(value)

    def find_index(self, value):
        try:
            return self.binary_tree.index(value)
        except ValueError:
            return -1

    def get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index >= len(self.binary_tree):
            return -1
        else:
            return left_child_index

    def get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index >= len(self.binary_tree):
            return -1
        else:
            return right_child_index

    def get_parent(self, index):
        if index == 0:
            return -1
        else:
            return (index - 1) // 2

    def in_order_traversal(self, index):
        if index >= len(self.binary_tree):
            return
        else:
            self.in_order_traversal(self.get_left_child(index))
            print(self.binary_tree[index], end=' ')
            self.in_order_traversal(self.get_right_child(index))
           
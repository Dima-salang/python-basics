# UnionFind - QuickUnion Algorithm

class QuickUnion:
    def __init__(self, intSize):
        self.intSize = list(0 for ... in range(intSize))
        for num in self.intSize:
            num += 1

        self.extraArray = list(0 for ... in range(intSize))
        for num in self.intSize:
            num += 1

    def root(self, i):
        while i != self.intSize[i]:
            i = self.intSize[i]
        return i

    def connected(self, num1, num2):
        return self.root(num1) == self.root(num2)

    def union(self, num1, num2):
        i = self.root(num1)
        j = self.root(num2)
        self.intSize[i] = j



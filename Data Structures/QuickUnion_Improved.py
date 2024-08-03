class QuickUnionImproved:

    # weighted quick union with path compression...

    def __init__(self, intSize):
        self.items = list(range(intSize))
        self.sizes = list(range(intSize))

    def root(self, i):
        while i != self.items[i]:
            self.items[i] = self.items[self.items[i]] # make every other node in path point to its grandparent
            i = self.items[i]
        return i

    def find(self, num1, num2):
        return self.root(num1) == self.root(num2)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        elif self.sizes[i] < self.sizes[j]:
            self.items[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.items[j] = i
            self.sizes[i] += self.sizes[j]


QU = QuickUnionImproved(10)
QU.union(9, 3)
QU.union(8, 3)
print(QU.root(3))
print(QU.root(9))
print(QU.root(8))
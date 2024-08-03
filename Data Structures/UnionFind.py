class UnionFind:  # QuickFind Algorithm
    def __init__(self, intSize):
        self.intSize = list(0 for ... in range(intSize))
        for num in self.intSize:
            num += 1

    def connected(self, num1, num2):
        return self.intSize[num1] == self.intSize[num2]

    def union(self, num1, num2):
        union1 = self.intSize[num1]
        union2 = self.intSize[num2]
        if union1 != union2:
            for value in self.intSize:
                if value == union2:
                    valIndex = self.intSize.index(value)
                    self.intSize[valIndex] = union1
        else:
            self.connected(num1, num2)

    # Quick-find is too slow.
    # Cost model: Number of array accesses: Initialize = N, Union = N, Find = 1
    # Quick-find defect - Union too expensive. Takes N^2 array accesses to process
    # sequence of N union commands on N objects. The algorithm is quadratic.






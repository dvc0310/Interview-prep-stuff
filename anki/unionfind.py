class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        self.max = list(range(size))

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def find_Max(self, node):
        root = self.find(node)
        self.max[node] = self.max[root]
        return self.max[node]
    
    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
    
    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        max1 = self.find_Max(root1)
        max2 = self.find_Max(root2)

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            self.max[root1] = max(max1, max2)
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            self.max[root2] = max(max1, max2)





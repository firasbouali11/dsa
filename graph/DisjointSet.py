class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    def findParent(self, i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.findParent(self.parent[i])
        return self.parent[i]
    
    def unionBySize(self, u, v):
        parent_u = self.parent[u]
        parent_v = self.parent[v]
        if parent_u == parent_v: return
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
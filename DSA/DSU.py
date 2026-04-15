#Basic Implementation of Disjoint Set Union (DSU) or Union-Find data structure

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px


#Union By Rank Optimization

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # cycle detected

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True



from typing import List, Tuple

def kruskal(n: int, edges: List[Tuple[int, int, int]]):
    """
    n: number of vertices
    edges: list of (u, v, weight)
    returns: (total_weight, mst_edges)
    """
    dsu = DisjointSet(n)
    edges.sort(key=lambda edge: edge[2])  # sort by weight

    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

            # MST is complete when we have n - 1 edges
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges


edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]

n = 6
total_weight, mst = kruskal(n, edges)

print("MST Weight:", total_weight)
print("MST Edges:", mst)

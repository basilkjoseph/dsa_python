"""
Kruskal's Minimum Spanning Tree (MST) implementation using a Disjoint Set (Union-Find).

This module contains:
- DisjointSet: a union-find data structure with path compression and union by rank
- kruskal: function that computes the MST of an undirected weighted graph

The example at the bottom demonstrates basic usage (guarded by __main__).
"""

from typing import List, Tuple


class DisjointSet:
    """Disjoint Set (Union-Find) with path compression and union by rank."""

    def __init__(self, n: int):
        # parent[i] is the parent of node i; initially each node is its own parent
        self.parent = list(range(n))
        # rank is an upper bound on the height of the tree for union by rank
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """Find the representative (root) of the set that contains x.

        Uses path compression to flatten the tree, making subsequent finds faster.
        """
        if self.parent[x] != x:
            # Recursively find the root and compress the path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union the sets that contain x and y.

        Returns True if a union was performed (i.e., x and y were in different sets).
        Returns False if x and y were already in the same set (would form a cycle).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # No union performed: x and y already connected

        # Attach the smaller tree to the root of the larger tree (union by rank)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: choose one root and increase its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Compute the Minimum Spanning Tree (MST) weight and edges using Kruskal's algorithm.

    Parameters:
    - n: number of vertices (assumed labeled 0..n-1)
    - edges: list of (u, v, weight) tuples representing undirected edges

    Returns:
    - (total_weight, mst_edges): total weight of the MST and the list of edges included

    Complexity:
    - Time: O(E log E) dominated by sorting the edges (E = number of edges)
    - Space: O(V) for the disjoint set and output storage
    """
    dsu = DisjointSet(n)

    # Sort edges by weight (ascending) so we always consider the smallest remaining edge
    edges.sort(key=lambda edge: edge[2])

    mst_weight = 0
    mst_edges: List[Tuple[int, int, int]] = []

    for u, v, weight in edges:
        # If u and v are in different components, include this edge in the MST
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

            # MST is complete when it has exactly n - 1 edges
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges


# Example usage (will only run when executed as a script)
if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
    ]

    n = 6
    total_weight, mst = kruskal(n, edges)

    print("MST Weight:", total_weight)
    print("MST Edges:", mst)

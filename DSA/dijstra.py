import heapq

def dijkstra(graph, source):
    """
    Dijkstra's algorithm to find the shortest path from source to all other nodes.
    
    Parameters:
    -----------
    graph: dict[int, list[tuple[int, int]]]
           adjacency list representation where graph[u] = [(v, weight), ...]
           u is the source node, v is the destination node, and weight is the edge weight
    source: int
            starting node for shortest path calculation

    Returns:
    --------
    dict[node] = shortest distance from source to each node
    """
    # Initialize distances from source to all nodes as infinity
    # Set source distance to 0 as it's the starting point
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    # Min-heap stores tuples of (distance, node) for efficient extraction
    # Always extracts the node with the smallest distance first
    pq = [(0, source)]

    # Process nodes in order of their distance from source
    while pq:
        # Extract the node with minimum distance from priority queue
        curr_dist, u = heapq.heappop(pq)

        # Skip this entry if we've already found a shorter path to node u
        # This optimization avoids reprocessing outdated entries in the heap
        if curr_dist > dist[u]:
            continue

        # Explore all neighbors of the current node
        for v, weight in graph[u]:
            # Calculate the distance to neighbor v through current node u
            new_dist = curr_dist + weight

            # If we found a shorter path to v, update its distance and add to heap
            # This relaxation step ensures we explore better paths first
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # Return dictionary mapping each node to its shortest distance from source
    return dist

from sys import maxsize
from queue import PriorityQueue

from DisjointSet import DisjointSet

def dijkstra(graph, start, n):
    queue = PriorityQueue()
    queue.put((0, start))
    distance = [maxsize for _ in range(n)]
    distance[start] = 0
    while not queue.empty():
        _, node = queue.get()
        for w, adj in graph[node]:
            if distance[node] + w < distance[adj]:
                distance[adj] = distance[node] + w
                queue.put((distance[adj], adj))
    return distance

def bellmanFord(edges, start, v):
    distance = [maxsize for _ in range(v)]
    distance[start] = 0
    for _ in range(v-1):
        for s, e, w in edges:
            distance[e] = min(distance[e], distance[s] + w)
    #check for negitive cycles
    for s, e, w in edges:
        if distance[s] + w < distance[e]: return [-1]
    
    return distance

def prim(graph, start, n):
    mst = []
    visited = [0] * n
    s = 0
    queue = PriorityQueue()
    queue.put((0, start, -1))
    while not queue.empty():
        w, node, parent = queue.get()
        if visited[node]: continue
        visited[node] = 1
        s += w
        if parent != -1:
            mst.append((node, parent))
        for adj_w, adj in graph[node]:
            if not visited[adj]:
                queue.put((adj_w, adj, node))
    
    return mst, s

def kruskal(graph, n):
    edges = []
    for node in graph:
        for w, adj in graph[node]:
            edges.append((w, node, adj))
    ds = DisjointSet(n)
    mst = []
    s = 0
    edges.sort()
    for w, u, v in edges:
        if ds.findParent(u) != ds.findParent(v):
            s+=w
            mst.append((u, v))
            ds.unionBySize(u, v)
    return mst, s
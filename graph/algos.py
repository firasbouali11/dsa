from sys import maxsize
from queue import PriorityQueue

from DisjointSet import DisjointSet
from operations import topoSort
from traversals import dfs

#find shortest path in a graph with no negative weights
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

#find shortest path in a graph
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

#find mst
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

#find mst
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

#find number of strongly connected components
def kosaraju(graph):
    visited = [False] * (len(graph))
    stack = []
    reversed_graph = {}
    #sort the edges by the time of finish (toposort)
    topoSort(graph, 0, visited, stack)
    #reverse the graph
    for node, adjs in enumerate(graph):
        visited[node] = False
        for adj in adjs:
            if adj in reversed_graph:
                reversed_graph[adj].append(node)
            else:
                reversed_graph[adj] = [node]
    count = 0
    #do a dfs
    while stack:
        node = stack.pop()
        if not visited[node]:
            count+=1
            dfs(node)
    return count
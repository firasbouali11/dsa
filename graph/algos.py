from sys import maxsize
from queue import PriorityQueue

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
    pass
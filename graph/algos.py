from sys import maxsize


def dijkstra(graph, start, n):
    queue = {(0, start)}
    distance = [maxsize for _ in range(n)]
    distance[start] = 0
    while queue:
        _, node = queue.pop()
        for w, adj in graph[node]:
            if distance[node] + w < distance[adj]:
                if distance[adj] != maxsize:
                    queue.remove((distance[adj], adj))
                distance[adj] = distance[node] + w
                queue.add((adj, distance[adj]))
    return distance

def bellmanFord(edges, start, v):
    distance = [1e9 for _ in range(v)]
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

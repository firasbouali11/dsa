from sys import maxsize
from collections import deque


def isCyclicBFS(graph):
    vis = [False for _ in graph]
    queue = deque([(0, -1)])
    vis[0] = True 
    while queue:
        node, parent = queue.popleft()
        for adj in graph[node]:
            if not vis[adj]:
                vis[adj] = True
                queue.append((adj, node))
            elif parent != adj: return True
    return False 

def isCyclicDFS(graph, node, vis, parent=-1): # for Undirected Graphs
    vis[node] = True
    for adj in graph[node]:
        if not vis[adj]:
            isCyclicDFS(graph, adj, vis, node)
        elif parent != adj: return True
    return False

def isCyclicDG(graph, node, visited, path): # for Directed Graphs
    visited[node] = True
    path[node] = True
    for adj in graph:
        if not visited[adj]:
            if isCyclicDG(graph, adj, visited, path): return True
        else:
            if path[adj]: return True
    path[node] = False
    return False

def isBipartite(graph):
    colors = [-1 for _ in graph]
    queue = deque([0])
    colors[0] = False
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if colors[adj] == -1:
                colors[adj] = not colors[node]
                queue.append(adj)
            elif colors[adj] == colors[node]:
                return False
    return True

#dfs
def topoSort(graph, node, vis, stack): # only applicable in DAG
    vis[node] = True
    for adj in graph[node]:
        if not vis[adj]:
            topoSort(graph, adj, vis, stack)
    stack.append(node) # the answer is the reverse of the stack

def shortestDistanceTopoSort(graph, start, n):  # for DAG
    stack = []
    visited = [False for _ in range(n)]
    distance = [maxsize for _ in range(n)]
    distance[start] = 0
    topoSort(graph, start, visited, stack)
    while stack:
        node = stack.pop()
        for adj, w in graph[node]:
            distance[adj] = min(distance[node] + w, distance[adj])
    
    return distance
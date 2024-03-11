from collections import deque

def bfs(graph):
    queue = deque([0])
    visited = [False for _ in graph]
    visited[0] = True
    while queue:
        node = queue.popleft()
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
        #extra action

def dfs(graph, i, visited):
    visited[i] = True
    #extra action
    for adj in graph[i]:
        if not visited[adj]:
            dfs(graph, adj, visited)
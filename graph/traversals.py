from collections import deque

def bfs(graph):
    queue = deque([0])
    visited = [False] * len(graph)
    visited[0] = True
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)
        #extra action

def dfs(graph, i, visited):
    visited[i] = True
    #extra action
    for adj in graph[i]:
        if not visited[adj]:
            dfs(graph, adj, visited)
graph = [
    [2],
    [2],
    [3,4],
    [1],
    []
]

def bfs(graph):
    queue = [0]
    visited = [False for _ in graph]
    visited[0] = True
    while queue:
        node = queue.pop()
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
        print(node, end = " ")
    print()

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=" ")
    for adj in graph[i]:
        if not visited[adj]:
            dfs(graph, adj, visited) 


bfs(graph)
visited = [False for _ in graph]
dfs(graph, 0, visited)
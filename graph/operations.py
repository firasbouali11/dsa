def isCyclicBFS(graph):
    vis = [False for _ in graph]
    queue = [(0, -1)]
    vis[0] = True 
    while queue:
        node, parent = queue.pop()
        for adj in graph[node]:
            if not vis[adj]:
                vis[adj] = True
                queue.append((adj, node))
            elif parent != adj: return True
    return False 

def isCyclicDFS(graph, node, vis, parent=-1):
    vis[node] = True
    for adj in graph[node]:
        if not vis[adj]:
            isCyclicDFS(graph, adj, vis, node)
        elif parent != adj: return True
    return False

def isBipartite(graph):
    colors = [-1 for _ in graph]
    queue = [0]
    colors[0] = False
    while queue:
        node = queue.pop(0)
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


if __name__ == "__main__":
    graph = [
        [1,3],
        [0,2],
        [1,3],
        [0,4,2],
        [3]
    ]   
    print(isCyclicBFS(graph)) #true
    vis = [False for _ in graph]
    print(isCyclicDFS(graph,0,vis)) #true
    non_bp_graph = [
        [1],
        [0,2,3],
        [1,5],
        [1,4],
        [3,5],
        [2,4],
    ]
    print(isBipartite(graph))
    print(isBipartite(non_bp_graph))

    stack = []
    graph = [
        [1,3],
        [2],
        [3],
        [],
    ]
    vis = [False for _ in graph]
    topoSort(graph, 0, vis, stack)
    print(stack[::-1])

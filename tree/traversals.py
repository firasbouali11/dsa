from collections import deque
"""
preorder traversal root, left, right
inorder traversal  left, root, right
postrder traversal left, right, root
"""
# preorder traversal
def dfs(node):
    if node == None: return
    print(node.data, end = " ")
    dfs(node.left)
    dfs(node.right)

#by levels
def bfs(root):
    ans = []
    if root == None: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        ans.append(node)
    print(ans)
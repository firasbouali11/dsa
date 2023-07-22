from structure import TreeNode

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
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            level.append(node.data)
        ans.append(level)
    for node in ans:
        print(node)

node3 = TreeNode(4)
node1 = TreeNode(3)
node2 = TreeNode(2, node3)
root = TreeNode(1, node1, node2)
root2 = TreeNode(1, node1)

dfs(root)
print("")
bfs(root)

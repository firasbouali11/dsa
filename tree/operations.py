from structure import TreeNode

def maxDepth(node):
    if node == None: return 0
    l = maxDepth(node.left)
    r = maxDepth(node.right)
    return 1 + max(l,r)

def checkBalancedTree(node):
    if node == None: return True
    l = maxDepth(node.left)
    r = maxDepth(node.right)
    if(abs(l-r) > 1): return True
    return False

def identicalTrees(tree1, tree2):
    if tree1 == None or tree2 == None:
        return tree1 == tree2
    return tree1.data == tree2.data and\
          identicalTrees(tree1.left, tree2.left) and\
              identicalTrees(tree1.right, tree2.right)

def getPathToNode(node, k):
    if node == None: return []
    if node.data == k:
        return [node.data]
    l = getPathToNode(node.left, k)
    if len(l) != 0:
        return [node.data] + l
    r = getPathToNode(node.right, k)
    if len(r) != 0:
        return [node.data] + r
    return []

def lca(node):
    pass

node3 = TreeNode(4)
node1 = TreeNode(3)
node2 = TreeNode(2, node3)
root = TreeNode(1, node1, node2)
root2 = TreeNode(1, node1)

print(maxDepth(root))
print(checkBalancedTree(root))
print(identicalTrees(root, root))
print(identicalTrees(root, root2))
print(getPathToNode(root, 4))

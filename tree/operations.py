from sys import maxsize

def maxDepth(node):
    if node == None: return 0
    l = maxDepth(node.left)
    r = maxDepth(node.right)
    return 1 + max(l,r)

def maxWidth(node):
    depth = maxDepth(node)
    return 2**(depth-1)

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

def lca(root, x, y):
    if root == None or root.data == x or root.data == y: return root
    l = lca(root.left, x, y)
    r = lca(root.right, x, y)
    if l is None: return r
    elif r is None: return l
    else: return root
  
def isBST(root, l = -1 * maxsize, h = maxsize):
    if root is None: return True
    if not(l < root.data < h): return False
    if not isBST(root.left, l, root.data): return False
    if not isBST(root.right, root.data, h): return False
    return True

def searchInBST(root, k):
    temp = root
    while temp is not None:
        if temp.data == k:
            return True
        elif temp.data > k:
            temp = temp.left
        else: temp = temp.right
    return False
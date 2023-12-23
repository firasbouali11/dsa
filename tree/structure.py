class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def buildTree(preorder, inorder):
        mpp = {}
        n = len(inorder)
        for i in range(n):
            mpp[inorder[i]] = i

        def f(sp, ep, si, ei):
            if sp > ep or si > ei: return None
            root = TreeNode(preorder[sp])
            root_ind = mpp[root.data]
            other = root_ind - si
            root.left = f(sp +1, sp + other, si, root_ind-1)  
            root.right = f(sp + other +1, ep, root_ind+1, ei)  
            return root  
        
        return f(0, n-1, 0, n-1)
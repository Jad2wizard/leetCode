# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr = []
        res = []
        if root:
            root.depth = self.rootDepth(root)
            for i in range(root.depth):
                res.append([])
            arr.append(root)
        
        while len(arr) is not 0:    
            tmp = arr.pop()
            res[-tmp.depth].append(tmp.val)
            if tmp.right:
                tmp.right.depth = tmp.depth - 1
                arr.append(tmp.right)
            if tmp.left:
                tmp.left.depth = tmp.depth -1
                arr.append(tmp.left)
        
        return res     
    
    def rootDepth(self, root):
        if not root:
            return 0
        left = self.rootDepth(root.left)
        right = self.rootDepth(root.right)
        return 1 + (left if left > right else right)

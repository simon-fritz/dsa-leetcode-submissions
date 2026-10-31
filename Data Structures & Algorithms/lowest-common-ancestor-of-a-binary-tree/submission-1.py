# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node):
            if not node or node == p or node == q:
                return node
            l = findLCA(node.left)
            r = findLCA(node.right)
            if r and l:
                return node
            return r or l
        return findLCA(root)
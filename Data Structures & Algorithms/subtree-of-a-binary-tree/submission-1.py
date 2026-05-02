# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isIdentical(self, t1: Optional[TreeNode], t2: Optional[TreeNode]):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        if t1.val != t2.val:
            return False
        return self.isIdentical(t1.right,t2.right) and self.isIdentical(t1.left,t2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            return self.isIdentical(root,subRoot) or self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        return False
        

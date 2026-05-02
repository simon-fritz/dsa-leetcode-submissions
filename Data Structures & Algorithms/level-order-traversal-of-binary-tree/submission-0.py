# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            res.append([n.val for n in stack])
            newstack = []
            for n in stack:
                if n.left: newstack.append(n.left)
                if n.right: newstack.append(n.right)
            stack = newstack
        return res
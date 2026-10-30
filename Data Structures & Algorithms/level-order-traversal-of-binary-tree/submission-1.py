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
        stack = [root]
        res = [[]]
        while stack:
            newStack = []
            for n in stack:
                res[-1].append(n.val)
                if n.left:
                    newStack.append(n.left)
                if n.right:
                    newStack.append(n.right)
            res.append([])
            stack = newStack
        res.pop()
        return res

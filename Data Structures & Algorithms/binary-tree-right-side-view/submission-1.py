# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack=[root]
        res=[]
        while stack:
            res.append(stack[-1].val)
            newstack = []
            for n in stack:
                if n.left: newstack.append(n.left)
                if n.right: newstack.append(n.right)
            stack = newstack
        return res

        
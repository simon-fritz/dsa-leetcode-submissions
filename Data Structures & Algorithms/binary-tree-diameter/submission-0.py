# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return -1
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            path = left + right
            #update max
            nonlocal maxDia
            maxDia = max(maxDia,path)
            return max(left,right)
        dfs(root)
        return maxDia
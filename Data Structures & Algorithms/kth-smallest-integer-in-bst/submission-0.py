class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = []
        def inorder(root: Optional[TreeNode]):
            if not root or len(counter) == k:
                return
            inorder(root.left)
            if len(counter) < k:
                counter.append(root.val)
            inorder(root.right)
        inorder(root)
        return counter[-1]
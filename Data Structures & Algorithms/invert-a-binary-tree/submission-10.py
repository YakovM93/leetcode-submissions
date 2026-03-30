class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        rever = root
        temp = root.left
        rever.left = self.invertTree(root.right)
        rever.right = self.invertTree(temp)

        return rever
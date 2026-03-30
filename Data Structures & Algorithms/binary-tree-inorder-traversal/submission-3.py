class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        arr.extend(self.inorderTraversal(root.left))
        arr.append(root.val)
        arr.extend(self.inorderTraversal(root.right))
        return arr
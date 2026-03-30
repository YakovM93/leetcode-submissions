
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum) or
                (not targetSum and not root.left and not root.right))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')
            
        def helper(node):
            # returns the best sum of a path that starts
            # at this node and goes DOWN (one direction only)
            nonlocal best
            if not node:
                return 0

            left = max(helper(node.left), 0)   # ignore negative paths
            right = max(helper(node.right), 0)

            # the "arch" through this node — candidate for answer
            arch = node.val + left + right
            best = max(best, arch)

            # return the best single-direction path (for parent to use)
            return node.val + max(left, right)
        helper(root)
        return best

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            stack = []
            curr = root
            n = 0
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                n += 1
                if n == k:
                    return curr.val
                curr = curr.right
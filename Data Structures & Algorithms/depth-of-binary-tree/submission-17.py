# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        maxi = 0
        temp = 0
        curr =  root
        stack = []

        while curr or stack:
             
            if curr:
                temp += 1
                stack.append((curr, temp))
                curr = curr.left
                
            else:
                curr, temp = stack.pop()
                maxi = max(maxi, temp)

                curr =  curr.right
        return maxi        



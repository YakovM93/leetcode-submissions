class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, root.val)])
        count = 0

        while q:
            node, maxi = q.popleft()
            if node.val >= maxi:
                count += 1
            
            new_max = max(maxi, node.val)
            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))

        return count
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            queue = deque()
            bfs_list = []
            
            if root:
                queue.append(root)
            while len(queue) > 0:
                level_nodes = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    level_nodes.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right) 
                bfs_list.append(level_nodes)    
            
            return bfs_list
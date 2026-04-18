class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word

        ress = set()
        path = set()

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            
            next_node = node[char]
            if '#' in next_node:
                ress.add(next_node['#'])
                # Optimization: remove found word from trie to avoid redundant work
            
            path.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in path:
                    dfs(nr, nc, next_node)
            path.remove((r, c))
            
            if not next_node:
                node.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie)

        return list(ress)
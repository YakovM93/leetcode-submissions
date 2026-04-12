class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_count, close_count, Str):
            if len(Str) == 2 * n:
                res.append(Str)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, Str + "(")
            if close_count < open_count:
                dfs(open_count, close_count + 1, Str + ")")
        
        dfs(0, 0, "")
        return res
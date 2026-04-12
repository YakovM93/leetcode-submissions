class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(n, array):
            if sum(array) == target:
                    result.append(list(array))
                    return
            if sum(array) > target:
                    return
            for i in range(n, len(candidates)):  
                if i > n and candidates[i] == candidates[i-1]:
                    continue
                else:    
                    array.append(candidates[i])
                    dfs(i + 1, array)
                    array.pop()

        dfs(0, [ ])
        return result
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(n, array):
            result.append(list(array))
            for i in range(n, len(nums)):
                array.append(nums[i])
                dfs(i+1, array)
                array.pop()    
        dfs(0, [])    
        return result
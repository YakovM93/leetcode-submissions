class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(n, array):
            if sum(array) == target:
                    result.append(list(array))
                    return
            if sum(array) > target:
                    return
            for i in range(n, len(nums)):  
                array.append(nums[i])
                dfs(i, array)
                array.pop()

        dfs(0, [ ])
        return result
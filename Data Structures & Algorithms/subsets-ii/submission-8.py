class Solution:    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, array):
            if i >= len(nums):
                result.append(list(array))
                return

            # Include nums[i]
            array.append(nums[i])
            dfs(i + 1, array)
            array.pop()
            
            # Skip duplicates and move to next unique element
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, array)

        dfs(0, [])
        return result
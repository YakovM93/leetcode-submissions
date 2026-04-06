class Solution:    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, array):
            if i >= len(nums):
                result.append(list(array))
                return 
            
            # Decision to include nums[i]
            array.append(nums[i])
            dfs(i+1, array)
            array.pop()        

            # Decision NOT to include nums[i] and skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, array)       

        dfs(0, [])
        return result
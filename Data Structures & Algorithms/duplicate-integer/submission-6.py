class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dici = set(nums)
        return len(nums) != len(dici)
   

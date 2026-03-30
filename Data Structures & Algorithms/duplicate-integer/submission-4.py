class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dici = set(nums)
        if len(nums) != len(dici):
            return True
        else :
            return False    

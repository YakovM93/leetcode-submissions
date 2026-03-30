class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici = {}
        for i, j in enumerate(nums):
            diff =  target - j
            if diff in dici:
                return [dici[diff],i]
            dici[j] = i    
            

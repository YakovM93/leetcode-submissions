class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici = {}
        #for i, j in enumerate(nums):
         #   diff =  target - j
          #  if diff in dici:
           #     return [dici[diff],i]
            #dici[j] = i    
        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff in dici:
                return [dici[diff],i]
            dici[nums[i]] = i      


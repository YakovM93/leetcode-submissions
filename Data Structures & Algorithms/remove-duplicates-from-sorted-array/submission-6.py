class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr =  [ ]
        for i in range(len(nums)):
             if nums[i] not in arr:
                arr.append(nums[i]) 
        nums[:len(arr)] = arr
        return len(arr)
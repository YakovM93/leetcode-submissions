class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0 for i in range(3)]
        for n in nums:
            counts[n] += 1
        k = 0
        for color in range(len(counts)):
            for count in range(counts[color]):
                nums[k] = color
                k += 1
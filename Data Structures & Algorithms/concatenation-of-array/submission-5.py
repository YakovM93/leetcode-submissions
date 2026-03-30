class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []  # Start with empty list
        
        for num in nums:
            ans.append(num)  # Add first copy
        
        for num in nums:
            ans.append(num)  # Add second copy
        
        return ans  
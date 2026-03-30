class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        max1 = 0
        l=0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max1 = max(max1, prices[r] - prices[l])
            r+=1    

        return max1
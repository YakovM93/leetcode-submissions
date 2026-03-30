class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        j = 0
        l,r = 0,len(heights)-1
        
        while l < r:
            area = (r-l) * min(heights[l],heights[r])  
            
            if area > maxarea:
                maxarea = area
            
            if heights[l] < heights[r]:
                l+= 1
            else:
                r -= 1

        return maxarea
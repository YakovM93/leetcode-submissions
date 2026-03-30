class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        length = len(heights)
        stack_area = 0
        for i in range(len(heights)):
            current_min = heights[i]
            for j in range(i, -1, -1):
                current_min = min(current_min, heights[j])
                width = i - j + 1
                max_area = max(max_area, current_min * width)

        return max_area
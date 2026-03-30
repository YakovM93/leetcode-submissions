class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = { ")": "(", "]": "[", "}": "{"}
        stack = []
       
        for char in s:
            if char in pair_map:
                top_element = stack.pop() if stack else '#'
                if pair_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
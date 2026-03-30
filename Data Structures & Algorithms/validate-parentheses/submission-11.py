class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = { ")": "(", "]": "[", "}": "{"}
        stack = []
       
        for char in s:
            if char in pair_map:
                if stack and stack[-1] == pair_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) 
        return True if not stack else False                    
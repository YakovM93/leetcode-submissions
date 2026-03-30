class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = 0
        length  = 1
        r = 1
        while r < len(s):
           
            while r < len(s) and s[r] not in s[l:r]:
                r+=1
                length =  max(r-l,length)
            l+=1
            if r <= l: r = l + 1
        return length
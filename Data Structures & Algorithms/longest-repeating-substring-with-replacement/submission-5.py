class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cou = {}
        l = 0 

        for r in range(len(s)):
            cou[s[r]] = 1 + cou.get(s[r], 0)
            while (r-l+1) - max(cou.values()) > k:
                cou[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res